# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PresentationProcessingAlgorithm
                                 A QGIS plugin
 Lallemand Plant Care
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-05-01
        git sha              : $Format:%H$
        copyright            : (C) 2023 by CamellOnCase
        email                : camelloncase@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os.path

from processing.gui.wrappers import WidgetWrapper
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProject,
                       QgsProcessing,
                       QgsProcessingParameterField,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterDefinition)

from ..help.algorithms_help import ProcessingAlgorithmHelpCreator
from ...constants import FETCH_ALL_TRIAL, FETCH_ONE_TRIAL, DIRECTORY_STRUCTURE
from ...factories.postgres_factory import PostgresFactory
from ...services.plot_service import PlotterService
from ...services.report_service import ReportService
from ...services.statistics_service import StatisticsService
from ...services.system_service import SystemService


class PresentationProcessingAlgorithm(QgsProcessingAlgorithm):

    TRIAL_NAME = 'TRIAL_NAME'
    T1_SURFACE = 'T1_SURFACE'
    T2_SURFACE = 'T2_SURFACE'
    YIELD_FIELD = 'YIELD_FIELD'
    T1_VALIDATION = 'T1_VALIDATION'
    T2_VALIDATION = 'T2_VALIDATION'
    GAIN_POINTS = 'GAIN_POINTS'
    OUTPUT = 'OUTPUT'

    def __init__(self):
        super().__init__()
        self.project = QgsProject.instance()
        self.postgresFactory = PostgresFactory()
        self.plotService = PlotterService()
        self.reportService = ReportService()
        self.systemService = SystemService()
        self.statisticsService = StatisticsService()

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """
        self.addParameter(
            ParameterTrialName(
                self.TRIAL_NAME,
                description="Trial name"
            )
        )

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.T1_SURFACE,
                self.tr('T1 surface points layer'),
                [QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.T2_SURFACE,
                self.tr('T2 surface points layer'),
                [QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterField(
                self.YIELD_FIELD,
                self.tr('Yield field'),
                parentLayerParameterName=self.T1_SURFACE,
                type=QgsProcessingParameterField.Any,
                allowMultiple=False,
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.T1_VALIDATION,
                self.tr('T1 validation layer'),
                [QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.T2_VALIDATION,
                self.tr('T2 validation layer'),
                [QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.GAIN_POINTS,
                self.tr('Gain points layer'),
                [QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterFile(
                self.OUTPUT,
                self.tr('Output folder'),
                QgsProcessingParameterFile.Folder
            )
        )

    @staticmethod
    def parameterAsTrial(parameters, name, context):
        return parameters[name]

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        trialId = self.parameterAsTrial(parameters, self.TRIAL_NAME, context)
        t1SurfaceLayer = self.parameterAsVectorLayer(parameters, self.T1_SURFACE, context)
        t2SurfaceLayer = self.parameterAsVectorLayer(parameters, self.T2_SURFACE, context)
        yieldField = self.parameterAsFields(parameters, self.YIELD_FIELD, context)
        t1ValidationLayer = self.parameterAsVectorLayer(parameters, self.T1_VALIDATION, context)
        t2ValidationLayer = self.parameterAsVectorLayer(parameters, self.T2_VALIDATION, context)
        gainLayer = self.parameterAsVectorLayer(parameters, self.GAIN_POINTS, context)
        outputFolder = self.parameterAsFile(parameters, self.OUTPUT, context)

        resultFolder = list(DIRECTORY_STRUCTURE.keys())[5]
        rootPath = os.path.join(self.project.homePath(), resultFolder)

        pValue, anovaStats = self.getAnovaStatistics(t1SurfaceLayer, t2SurfaceLayer, yieldField[0])
        gainStats = self.getGainStatistics(gainLayer, yieldField[0])
        self.plotService.createGainStatisticsTable(pValue, gainStats, anovaStats, True, rootPath)
        presentationData = self.getPresentationParameters(trialId, t1ValidationLayer, t2ValidationLayer, rootPath)

        self.reportService.createPresentation(presentationData, outputFolder)

        return {self.OUTPUT: None}

    def getGainStatistics(self, gainLayer, field):
        gainStatsList = list()
        gainStats = self.statisticsService.getGainStatistics(gainLayer, field)
        for statistic in gainStats:
            gainStatsList.append([f'{statistic:.2f}'])
        return gainStatsList

    def getAnovaStatistics(self, t1SurfaceLayer, t2SurfaceLayer, field):
        anovaStatsList = list()
        fValue, pValue = self.statisticsService.calculateAnovaTest(field, t1SurfaceLayer, t2SurfaceLayer)
        anovaStats = self.statisticsService.getAnovaStatistics(field, t1SurfaceLayer, t2SurfaceLayer)

        for statisticList in anovaStats:
            formattedStatisticList = [f'{statistic:.2f}' for statistic in statisticList]
            anovaStatsList.append(formattedStatisticList)

        return f'{pValue:.2f}', anovaStatsList

    def getPresentationParameters(self, trialId, t1ValidationLayer, t2ValidationLayer, rootPath):

        trialResult = self.postgresFactory.fetchOne(FETCH_ONE_TRIAL, trialId)

        t1Rmse = next(t1ValidationLayer.getFeatures()) if t1ValidationLayer.featureCount() > 0 else None
        t2Rmse = next(t2ValidationLayer.getFeatures()) if t2ValidationLayer.featureCount() > 0 else None

        histogramPath = os.path.join(rootPath, DIRECTORY_STRUCTURE['05_Results'][0])
        variogramPath = os.path.join(rootPath, DIRECTORY_STRUCTURE['05_Results'][1])
        mapsPath = os.path.join(rootPath, DIRECTORY_STRUCTURE['05_Results'][2])

        presentationData = {
            1: {1: f"Area: {trialResult[0]['field_name']}"},
            2: {
                10: self.systemService.filterByFileName(mapsPath, ['01_Points_with_measured_yield_values']),
                11: self.systemService.filterByFileName(mapsPath, ['02_T1_Measured_yield']),
                12: self.systemService.filterByFileName(mapsPath, ['03_T2_Measured_yield'])},
            3: {
                10: self.systemService.filterByFileName(histogramPath, ['Yield_Map_V']),
                11: self.systemService.filterByFileName(histogramPath, ['T1_total_V']),
                12: self.systemService.filterByFileName(histogramPath, ['T2_total_V'])},

            5: {
                10: self.systemService.filterByFileName(mapsPath, ['06_Model_T1_T2']),
                11: self.systemService.filterByFileName(mapsPath, ['07_Model_T1']),
                12: self.systemService.filterByFileName(mapsPath, ['08_Model_T2']),
                13: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T1_T2_total_']),
                14: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T1_total_']),
                15: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T2_total_'])},
            6: {
                10: self.systemService.filterByFileName(mapsPath, ['04_T1_Sample_for_model_generation']),
                11: self.systemService.filterByFileName(mapsPath, ['07_Model_T1']),
                12: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T1_80_perc_']),
                13: self.systemService.filterByFileName(histogramPath, ['T1_80_perc_H']),
                15: f"RMSE = {t1Rmse['%_rmse']:.2f}%"},

            7: {
                10: self.systemService.filterByFileName(mapsPath, ['05_T2_Sample_for_model_generation']),
                11: self.systemService.filterByFileName(mapsPath, ['08_Model_T2']),
                12: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T2_80_perc_']),
                13: self.systemService.filterByFileName(histogramPath, ['T2_80_perc_H']),
                15: f"RMSE = {t2Rmse['%_rmse']:.2f}%"},
            8: {
                10: self.systemService.filterByFileName(mapsPath, ['11_Yield_gain_using_T2']),
                11: self.systemService.filterByFileName(rootPath, ['Yield_Gain_Histogram']),
                12: self.systemService.filterByFileName(rootPath, ['Gain_Statistics_Table'])}
        }

        return presentationData

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'createpresentation'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Create presentation')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Report')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'report'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return ProcessingAlgorithmHelpCreator.shortHelpString(self.name())

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('PresentationProcessingAlgorithm', string)

    def createInstance(self):
        return PresentationProcessingAlgorithm()


class TrialNameWidgetWrapper(WidgetWrapper):
    def __init__(self, *args, **kwargs):
        super(TrialNameWidgetWrapper, self).__init__(*args, **kwargs)

    def createWidget(self):
        self.trialComboBox = QtWidgets.QComboBox()
        PostgresFactory().fetchDataToCombobox(self.trialComboBox, FETCH_ALL_TRIAL, ['field_name'], 'id')
        self.trialComboBox.dialogType = self.dialogType
        return self.trialComboBox

    def parentLayerChanged(self, layer=None):
        pass

    def setLayer(self, layer):
        pass

    def setValue(self, value):
        pass

    def value(self):
        return self.trialComboBox.itemData(self.trialComboBox.currentIndex())

    def postInitialize(self, wrappers):
        pass


class ParameterTrialName(QgsProcessingParameterDefinition):
    def __init__(self, name, description=""):
        super().__init__(name, description)

    def clone(self):
        copy = ParameterTrialName(self.name(), self.description())
        return copy

    def type(self):
        return self.typeName()

    @staticmethod
    def typeName():
        return "trialname"

    def checkValueIsAcceptable(self, value, context=None):
        return True

    def metadata(self):
        return {
            "widget_wrapper": "lallemand_plant_care.core.algorithms.report.presentation_algorithm.TrialNameWidgetWrapper"
        }

    def valueAsPythonString(self, value, context):
        return str(value)

    def asScriptCode(self):
        raise NotImplementedError()

    @classmethod
    def fromScriptCode(cls, name, description, isOptional, definition):
        raise NotImplementedError()
