# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ExportMapsProcessingAlgorithm
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
from qgis.core import QgsProject
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QImageWriter
from qgis.core import (QgsProcessingAlgorithm,
                       QgsProcessingMultiStepFeedback,
                       QgsProcessingOutputNumber,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterNumber,
                      )
from processing.core.ProcessingConfig import ProcessingConfig

from ...constants import QGIS_TOC_GROUPS
from ...factories.postgres_factory import PostgresFactory
from ...services.composer_service import ComposerService
from ...services.layer_service import LayerService
from ...services.message_service import MessageService
from ...services.plot_service import PlotterService
from ...services.report_service import ReportService
from ...services.statistics_service import StatisticsService
from ...services.system_service import SystemService
from ...tools.algorithm_runner import AlgorithmRunner
from ....gui.settings.options_settings_dlg import OptionsSettingsPage


class ExportMapsProcessingAlgorithm(QgsProcessingAlgorithm):
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

    LAYOUTS = 'LAYOUTS'
    EXTENSION = 'EXTENSION'
    RESOLUTION = 'RESOLUTION'
    OUTPUT = 'OUTPUT'
    EXPORTED_LAYOUTS = 'EXPORTED_LAYOUTS'

    def __init__(self):
        super().__init__()
        self.layerService = LayerService()
        self.postgresFactory = PostgresFactory()
        self.statisticsService = StatisticsService()
        self.reportService = ReportService()
        self.systemService = SystemService()
        self.plotService = PlotterService()
        self.messageService = MessageService()

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.layoutList = sorted([composerLayout.name() for composerLayout in QgsProject.instance().layoutManager().printLayouts()],
                                 key=str.lower)
        self.addParameter(
            QgsProcessingParameterEnum(
                self.LAYOUTS,
                self.tr('Layouts to export'),
                options=self.layoutList,
                allowMultiple=True
            )
        )

        # self.addParameter(
        #     QgsProcessingParameterEnum(
        #         self.EXTENSION,
        #         self.tr('Extension for exported maps'),
        #         options=self.listFormats,
        #         defaultValue=ProcessingConfig.getSetting('DEFAULT_EXPORT_EXTENSION')
        #     )
        # )

        self.addParameter(
            QgsProcessingParameterNumber(
                self.RESOLUTION,
                self.tr('Export resolution (if not set, the layout resolution is used)'),
                optional=True,
                minValue=1
            )
        )

        self.addParameter(
            QgsProcessingParameterFile(
                self.OUTPUT,
                self.tr('Output folder where to save maps'),
                QgsProcessingParameterFile.Folder
            )
        )

        self.addOutput(
            QgsProcessingOutputNumber(
                self.EXPORTED_LAYOUTS,
                self.tr('Number of layouts exported')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        outputFolder = self.parameterAsFile(parameters, self.OUTPUT, context)
        layoutIds = self.parameterAsEnums(parameters, self.LAYOUTS, context)
        project = QgsProject.instance()

        layouts = project.layoutManager().printLayouts()

        composerService = ComposerService(project)

        multiFeedback = QgsProcessingMultiStepFeedback(len(layouts), feedback)
        total = 100.0 / len(layouts) if len(layouts) else 0

        if not os.path.isdir(outputFolder):
            multiFeedback.reportError(self.tr('\nERROR: No valid output folder given. We cannot continue...\n'))
        else:
            for layoutId in layoutIds:

                if multiFeedback.isCanceled():
                    self.messageService.criticalMessageBar('Exporting maps', 'operation aborted by the user!')
                    break
                layout = project.layoutManager().layoutByName(self.layoutList[layoutId])
                result = composerService.createLayoutExporter(layout, layout.name(), path=outputFolder)
                multiFeedback.pushInfo(self.tr(f'Exporting map from layout {layout.name()}.'))

                if result:
                    multiFeedback.pushInfo(self.tr('Map exported successfully!'))
                    self.messageService.logMessage(f'Exporting map from layout {layout.name()}: SUCCESS', 3)
                    feedback.setProgress(int(layoutId * total))
                else:
                    multiFeedback.reportError(self.tr('Map could not be exported!'))
                    self.messageService.logMessage(f'Exporting map from layout {layout.name()}: FAILED', 2)

        return {self.OUTPUT: None}

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'exportmaps'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Export maps')

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
        return QCoreApplication.translate('ExportMapsProcessingAlgorithm', string)

    def createInstance(self):
        return ExportMapsProcessingAlgorithm()
