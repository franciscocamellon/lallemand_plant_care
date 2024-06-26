# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RMSEProcessingAlgorithm
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
import math

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProject,
                       QgsProcessing,
                       QgsProcessingParameterField,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterVectorLayer)

from ..algorithm_runner import AlgorithmRunner
from ..help.algorithms_help import ProcessingAlgorithmHelpCreator
from ...services.layer_service import LayerService
from ...services.system_service import SystemService


class RMSEProcessingAlgorithm(QgsProcessingAlgorithm):

    VALIDATION_LAYER = 'VALIDATION_LAYER'
    VALIDATION_FIELD = 'YIELD_FIELD'
    ERROR_FIELD = 'ERROR_FIELD'
    OUTPUT = 'OUTPUT'

    def __init__(self):
        super().__init__()
        self.project = QgsProject.instance()
        self.layerService = LayerService()
        self.algRunner = AlgorithmRunner()
        self.systemService = SystemService()

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.VALIDATION_LAYER,
                self.tr('Validation points layer'),
                [QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterField(
                self.VALIDATION_FIELD,
                self.tr('Field to evaluate'),
                parentLayerParameterName=self.VALIDATION_LAYER,
                type=QgsProcessingParameterField.Any,
                allowMultiple=False,
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterField(
                self.ERROR_FIELD,
                self.tr('Field with square error'),
                parentLayerParameterName=self.VALIDATION_LAYER,
                type=QgsProcessingParameterField.Any,
                allowMultiple=False,
                optional=False
            )
        )


    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        validationLayer = self.parameterAsVectorLayer(parameters, self.VALIDATION_LAYER, context)
        validationField = self.parameterAsFields(parameters, self.VALIDATION_FIELD, context)
        errorField = self.parameterAsFields(parameters, self.ERROR_FIELD, context)

        errorStatistics = self.algRunner.runBasicStatisticsForFields(validationLayer,
                                                                     errorField[0],
                                                                     context=context,
                                                                     feedback=feedback)
        variableStatistics = self.algRunner.runBasicStatisticsForFields(validationLayer,
                                                                        validationField[0],
                                                                        context=context,
                                                                        feedback=feedback)
        rmse = math.sqrt(errorStatistics['SUM'] / errorStatistics['COUNT'])
        percentualRmse = (rmse / (variableStatistics['SUM'] / variableStatistics['COUNT'])) * 100

        return {self.OUTPUT: {'RMSE': rmse, 'PERCENTUAL_RMSE': percentualRmse}}

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'rmse'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('RMSE')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Statistics')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'statistics'

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
        return QCoreApplication.translate('RMSEProcessingAlgorithm', string)

    def createInstance(self):
        return RMSEProcessingAlgorithm()
