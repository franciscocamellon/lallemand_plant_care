# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TreatmentPolygons
                                 A QGIS plugin
 Lallemand Plant Care
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-10-07
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
import math
from typing import Optional

from qgis.utils import plugins
from qgis.PyQt import QtWidgets
from qgis.PyQt.Qt import QVariant
from qgis.core import QgsFieldProxyModel, QgsMapLayerProxyModel, QgsTask, QgsProcessingContext

from ...core.constants import VALIDATION_FIELDS, QGIS_TOC_GROUPS
from ...core.services.system_service import SystemService
from ...core.tools.algorithm_runner import AlgorithmRunner
from ...core.services.message_service import MessageService, UserFeedback
from .validation_dlg_base import Ui_Dialog
from ..settings.options_settings_dlg import OptionsSettingsPage
from ...core.services.layer_service import LayerService
from ...core.services.widget_service import WidgetService


class SamplingValidation(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, iface, project, parent=None):
        """Constructor."""
        super(SamplingValidation, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.project = project
        self.filePath = self.project.homePath()
        self.setWindowTitle('Sampling validation')
        self.layerService = LayerService()
        self.systemService = SystemService()
        self.context = QgsProcessingContext()
        self.settings = OptionsSettingsPage().getKrigingSettings()
        self.layers = self.project.instance().mapLayers()
        self.setValidationUi()
        self.setErrorCompensationUi()
        self.setGainSurfaceUi()
        self.validatePushButton.clicked.connect(self.runValidate)
        self.calculatePushButton.clicked.connect(self.runErrorCompensation)
        self.gainSurfacePushButton.clicked.connect(self.runGainSurface)

    def setValidationUi(self):
        samplingLayer = self.layerService.filterByLayerName(list(self.layers.values()), ['validation'])

        self.validationLayerComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.validationLayerComboBox.setExceptedLayerList(samplingLayer)

        self.krigingRasterComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)

        self.fieldToEstimateComboBox.setFilters(QgsFieldProxyModel.Numeric)
        self.fieldToEstimateComboBox.setLayer(self.validationLayerComboBox.currentLayer())
        validationFields = self.layerService.filterByFieldName(self.validationLayerComboBox.currentLayer(),
                                                               self.settings[0])
        self.fieldToEstimateComboBox.setFields(validationFields)

    def setErrorCompensationUi(self):
        treatmentRasters = self.layerService.filterByLayerName(list(self.layers.values()), ['80'])
        errorRasters = self.layerService.filterByLayerName(list(self.layers.values()), ['error', 'validation'])
        self.t1RasterComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.t2RasterComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.t1errorRasterComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.t2errorRasterComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)

        self.t1RasterComboBox.setExceptedLayerList(treatmentRasters)
        self.t2RasterComboBox.setExceptedLayerList(treatmentRasters)
        self.t1errorRasterComboBox.setExceptedLayerList(errorRasters)
        self.t2errorRasterComboBox.setExceptedLayerList(errorRasters)

    def setGainSurfaceUi(self):
        errorRasters = self.layerService.filterByLayerName(list(self.layers.values()), ['Final', 'surface'])
        self.t1FinalSurfaceComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.t2FinalSurfaceComboBox.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.t1FinalSurfaceComboBox.setExceptedLayerList(errorRasters)
        self.t2FinalSurfaceComboBox.setExceptedLayerList(errorRasters)

    @staticmethod
    def getRasterCalculatorParameters(expression, layer, filePath):

        return {'EXPRESSION': expression,
                'LAYERS': [layer],
                'CELLSIZE': 0,
                'EXTENT': None,
                'CRS': layer.crs().authid(),
                'OUTPUT': filePath}

    @staticmethod
    def getYieldPointsParameters(gainSurface, fieldName, filePath):
        return {
            'INPUT_RASTER': gainSurface,
            'RASTER_BAND': 1,
            'FIELD_NAME': fieldName,
            'OUTPUT': filePath
        }

    def runValidate(self):
        grid = self.krigingRasterComboBox.currentLayer()
        points = self.validationLayerComboBox.currentLayer()
        field = self.fieldToEstimateComboBox.currentField()
        self.close()
        print(field)
        feedback = UserFeedback(message='Validating...', title='Lallemand', parent=self)
        output = AlgorithmRunner().runAddRasterValuesToPoints(points, [grid], context=self.context, feedback=feedback)

        fieldName = self.systemService.getFieldName(grid.name())
        print(fieldName)
        total = 100.0 / output.featureCount() if output.featureCount() else 0
        output.startEditing()
        for index, feature in enumerate(output.getFeatures()):
            feature[VALIDATION_FIELDS[0]] = feature[fieldName]
            output.updateFeature(feature)
            if bool(feature[VALIDATION_FIELDS[0]]):
                feature[VALIDATION_FIELDS[1]] = feature[field] - feature[VALIDATION_FIELDS[0]]
                feature[VALIDATION_FIELDS[2]] = math.pow(feature[VALIDATION_FIELDS[1]], 2)
                output.updateFeature(feature)
            feedback.setProgress(int(index * total))
        output.commitChanges()
        output.triggerRepaint()

        errorStatistics = AlgorithmRunner().runBasicStatisticsForFields(output, VALIDATION_FIELDS[2],
                                                                        context=self.context,
                                                                        feedback=feedback)
        variableStatistics = AlgorithmRunner().runBasicStatisticsForFields(output, field,
                                                                           context=self.context,
                                                                           feedback=feedback)
        rmse = math.sqrt(errorStatistics['SUM'] / errorStatistics['COUNT'])
        percentualRmse = (rmse / (variableStatistics['SUM'] / variableStatistics['COUNT'])) * 100

        total = 100.0 / output.featureCount() if output.featureCount() else 0
        output.startEditing()
        for index, feature in enumerate(output.getFeatures()):
            if isinstance(feature[fieldName], QVariant):
                pass
            else:
                feature[VALIDATION_FIELDS[3]] = rmse
                feature[VALIDATION_FIELDS[4]] = percentualRmse
                output.updateFeature(feature)
            feedback.setProgress(int(index * total))
        output.commitChanges()
        output.triggerRepaint()

        fieldsToDelete = self.layerService.filterByFieldName(output, [fieldName], inverse=False)
        newOutput = self.layerService.deleteFields(output, fieldsToDelete)

        pointsProvider = points.dataProvider()
        points.selectAll()
        points.startEditing()
        points.deleteSelectedFeatures()
        featureList = [feature for feature in newOutput.getFeatures()]
        pointsProvider.addFeatures(featureList)
        points.commitChanges()
        points.triggerRepaint()
        points.invertSelection()

        feedback.close()

    def runErrorCompensation(self):
        self.close()
        t1FilePath = f"{self.filePath}/03_Error_Compensation/T1_Error_Compensation/T1_Final_Surface.tiff"
        t2FilePath = f"{self.filePath}/03_Error_Compensation/T2_Error_Compensation/T2_Final_Surface.tiff"
        t1Expression = f'"{self.t1RasterComboBox.currentLayer().name()}@1" + "{self.t1errorRasterComboBox.currentLayer().name()}@1"'
        t2Expression = f'"{self.t2RasterComboBox.currentLayer().name()}@1" + "{self.t2errorRasterComboBox.currentLayer().name()}@1"'
        t1Parameters = self.getRasterCalculatorParameters(t1Expression, self.t1RasterComboBox.currentLayer(),
                                                          t1FilePath)
        t2Parameters = self.getRasterCalculatorParameters(t2Expression, self.t2RasterComboBox.currentLayer(),
                                                          t2FilePath)

        feedback = UserFeedback(message='Validating...', title='Lallemand', parent=self)
        for parameter in [t1Parameters, t2Parameters]:

            finalSurface = AlgorithmRunner().runRasterCalculator(parameter, context=self.context, feedback=feedback)

            if self.surfacePointsCheckBox.isChecked():
                finalSurfacePointsParameters = self.getYieldPointsParameters(finalSurface, 'yield',
                                                                             f"{self.filePath}/03_Error_Compensation/T1_Error_Compensation/{finalSurface.name()}_Points.shp")

                finalSurfacePoints = AlgorithmRunner().runPixelsToPoints(finalSurfacePointsParameters,
                                                                         context=self.context, feedback=feedback)
                self.layerService.addMapLayer(finalSurfacePoints, QGIS_TOC_GROUPS[5])

            self.layerService.addMapLayer(finalSurface, QGIS_TOC_GROUPS[5])
            feedback.close()

    def runGainSurface(self):
        # self.yieldGainPointsCheckBox
        gainSurfacePath = f"{self.filePath}/04_Gain_Surface/Yield_Gain.tiff"
        expression = f'"{self.t2FinalSurfaceComboBox.currentLayer().name()}@1" - "{self.t1FinalSurfaceComboBox.currentLayer().name()}@1"'
        parameter = self.getRasterCalculatorParameters(expression, self.t1FinalSurfaceComboBox.currentLayer(),
                                                       gainSurfacePath)
        feedback = UserFeedback()
        gainSurface = AlgorithmRunner().runRasterCalculator(parameter, context=self.context, feedback=feedback)
        self.layerService.applySymbology(gainSurface, '', raster=True)
        self.layerService.addMapLayer(gainSurface, QGIS_TOC_GROUPS[6])

        if self.yieldGainPointsCheckBox.isChecked():
            pointsParameters = self.getYieldPointsParameters(gainSurface, 'yield',
                                                             f'{self.filePath}/04_Gain_Surface/Gain_Points.shp')
            gainPoints = AlgorithmRunner().runPixelsToPoints(pointsParameters, context=self.context, feedback=feedback)
            yieldGainHistogramPath = f"{self.filePath}/05_Results/Yield_Gain_Histogram.png"
            self.layerService.yieldGainFrequencyHistogram(gainPoints, yieldGainHistogramPath)
            self.layerService.addMapLayer(gainPoints, QGIS_TOC_GROUPS[6])

        feedback.close()
