# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SamplingProcessingAlgorithm
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
import os
from typing import Optional

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProject,
                       QgsFeatureSink,
                       QgsProcessing,
                       QgsProcessingParameterField,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingMultiStepFeedback)

from ..algorithm_runner import AlgorithmRunner
from ...constants import QGIS_TOC_GROUPS
from ...services.layer_service import LayerService
from ...services.system_service import SystemService
from ....gui.settings.options_settings_dlg import OptionsSettingsPage


class CreateSampleLayersProcessingAlgorithm(QgsProcessingAlgorithm):
    YIELD_FILTERED_LAYER = 'YIELD_FILTERED_LAYER'
    TREATMENT_FIELD = 'TREATMENT_FIELD'
    YIELD_FIELD = 'YIELD_FIELD'
    OUTPUT = 'OUTPUT'

    def __init__(self):
        super().__init__()
        self.project = QgsProject.instance()
        self.layerService = LayerService()
        self.algRunner = AlgorithmRunner()
        self.systemService = SystemService()
        self.treatmentSettings = OptionsSettingsPage()
        self.treatmentList: Optional[list] = None

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.YIELD_FILTERED_LAYER,
                self.tr('Yield filtered layer'),
                [QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterField(
                self.TREATMENT_FIELD,
                self.tr('Treatment field to filter'),
                parentLayerParameterName=self.YIELD_FILTERED_LAYER,
                type=QgsProcessingParameterField.Any,
                allowMultiple=False,
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterField(
                self.YIELD_FIELD,
                self.tr('Treatment field to filter'),
                parentLayerParameterName=self.YIELD_FILTERED_LAYER,
                type=QgsProcessingParameterField.Any,
                allowMultiple=False,
                optional=False
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        yieldLayer = self.parameterAsVectorLayer(parameters, self.YIELD_FILTERED_LAYER, context)
        treatmentField = self.parameterAsFields(parameters, self.TREATMENT_FIELD, context)
        yieldField = self.parameterAsFields(parameters, self.YIELD_FIELD, context)

        filePath = self.project.homePath()
        multiFeedback = QgsProcessingMultiStepFeedback(3, feedback)
        multiFeedback.pushInfo(self.tr(f'Initializing filtering...\n'))

        treatmentsDict = self.algRunner.runFilterTreatments(yieldLayer, treatmentField[0], 'TEMPORARY_OUTPUT', 'TEMPORARY_OUTPUT', context, feedback)

        for name, layer in treatmentsDict.items():
            treatmentPath = str()
            treatment = str()
            if name == 'T1_OUTPUT':
                treatment = 'T1'
                treatmentPath = os.path.join(filePath, '00_Data', '02_Sampling', f'{treatment}_total.shp')
            elif name == 'T2_OUTPUT':
                treatment = 'T2'
                treatmentPath = os.path.join(filePath, '00_Data', '02_Sampling', f'{treatment}_total.shp')

            self.layerService.saveVectorLayer(layer, treatmentPath)
            loadedLayer = self.layerService.loadShapeFile(QGIS_TOC_GROUPS[2], treatmentPath)
            self.layerService.applySymbology(loadedLayer, yieldField[0])

            sampleDict = self.algRunner.runSimpleSample(layer, context, feedback)

            for key, sampleLayer in sampleDict.items():
                group = QGIS_TOC_GROUPS[2] if key == 'SAMPLE_OUTPUT' else QGIS_TOC_GROUPS[4]
                treatmentSuffix = '80_perc' if key == 'SAMPLE_OUTPUT' else 'validation'
                middlePath = os.path.join('00_Data', '02_Sampling') if key == 'SAMPLE_OUTPUT' else '02_Validation'
                samplePath = os.path.join(filePath, middlePath, f'{treatment}_{treatmentSuffix}.shp')

                self.layerService.saveVectorLayer(sampleLayer, samplePath)

                if key == 'SAMPLE_OUTPUT':
                    loadedLayer = self.layerService.loadShapeFile(group, samplePath)
                    self.layerService.applySymbology(loadedLayer, yieldField[0])
                else:
                    self.layerService.loadShapeFile(group, samplePath)

        return {self.OUTPUT: None}

    @staticmethod
    def addToSink(features, sink, feedback):
        total = 100.0 / len(features) if len(features) else 0

        for current, feature in enumerate(features):
            if feedback.isCanceled():
                break

            sink.addFeature(feature, QgsFeatureSink.FastInsert)
            feedback.setProgress(int(current * total))

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'createsamplelayers'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Create sample layers')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Analysis')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'analysis'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Example algorithm short description")

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('CreateSampleLayersProcessingAlgorithm', string)

    def createInstance(self):
        return CreateSampleLayersProcessingAlgorithm()
