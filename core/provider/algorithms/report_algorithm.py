# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ReportProcessingAlgorithm
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

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterField,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterFile)
from qgis import processing

from ...constants import QGIS_TOC_GROUPS
from ...services.layer_service import LayerService
from ...services.system_service import SystemService
from ...tools.algorithm_runner import AlgorithmRunner
from ....gui.settings.options_settings_dlg import OptionsSettingsPage


class ReportProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    INPUT_FIELD = 'INPUT_FIELD'
    FOLDER_PATH = 'FOLDER_PATH'
    OUTPUT = 'OUTPUT'

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterField(
                self.INPUT_FIELD,
                self.tr('Field for variable of interest'),
                parentLayerParameterName=self.INPUT,
                type=QgsProcessingParameterField.Any,
                optional=False
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.FOLDER_PATH,
                self.tr('Directory path'),
                behavior=QgsProcessingParameterFile.Folder
            )
        )

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        self.layerService = LayerService()
        self.systemService = SystemService()
        self.treatments = OptionsSettingsPage().getTreatmentPolygonsSettings()

        inputLayer = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        layerAttribute = self.parameterAsString(parameters, self.INPUT_FIELD, context)
        filePath = self.parameterAsFile(parameters, self.FOLDER_PATH, context)

        reportData, tableData, imageData = self.getReportParameters()
        self.reportService.createWordReport(reportData, tableData, imageData, self.filePath,
                                            self.feedback)

        return {self.OUTPUT: dest_id}



    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'createreport'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Create Report')

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
        return self.tr("Example algorithm short description")

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('ReportProcessingAlgorithm', string)

    def createInstance(self):
        return ReportProcessingAlgorithm()