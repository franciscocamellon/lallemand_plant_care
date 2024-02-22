# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ToolbarManager
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
import os.path

from qgis.PyQt.QtCore import Qt, pyqtSlot
from qgis.PyQt.QtWidgets import QWidget, QToolButton, QMenu, QAction
from qgis.core import QgsMapLayer

from ..core.tools.algorithm_runner import AlgorithmRunner
from .filter.filtering_dlg import FilteringPoints
from .geostatistics_trial.geostatistics_trial import GeostatisticsTrial
from .kriging.kriging_dlg import OrdinaryKriging
from .layer_manager.load_files_dlg import LoadFiles
from .lpc_team.farmer_manager import FarmerManager
from .lpc_team.lpc_team_manager import RegisterLpcTeam
from .report.report_dlg import StatisticsReport
from .toolbar.toolbar_form_base import Ui_Form
from .treatment.treatment_polygons_dlg import TreatmentPolygons
from .validation.validation_dlg import SamplingValidation
from ..core.constants import QGIS_TOC_GROUPS
from ..core.services.layer_service import LayerService
from ..core.tools.composer_layout_runner import ComposerLayoutRunner
from ..core.tools.export_layout_runner import ExportLayoutRunner
from ..core.services.message_service import UserFeedback


class ToolbarManager(QWidget, Ui_Form):
    def __init__(self, iface, toolbar=None):
        """Constructor."""
        super(ToolbarManager, self).__init__()
        self.setupUi(self)
        self.iface = iface
        self.toolbar = toolbar
        self.actions = []
        self.layerService = LayerService()
        self.algRunner = AlgorithmRunner()
        self.splitter.hide()
        self.createTrialPushButton.clicked.connect(self.createTrialProject)
        self.loadFilePushButton.clicked.connect(self.loadFiles)
        self.lpcTeamPushButton.clicked.connect(self.manageLpcTeam)
        self.farmerPushButton.clicked.connect(self.manageFarmer)
        self.treatmentPushButton.clicked.connect(self.treatments)
        self.filterPushButton.clicked.connect(self.filtering)
        self.krigingPushButton.clicked.connect(self.ordinaryKriging)
        self.samplingValidationPushButton.clicked.connect(self.validation)
        self.clearStructurePushButton.clicked.connect(self.clearTreeView)
        self.reportPushButton.clicked.connect(self.getReport)
        self.mapsPushButton.clicked.connect(self.composer)
        self.exportMapPushButton.clicked.connect(self.exportMaps)

    def createToolButton(self, parent, text):
        """
        Creates a tool button (pop up menu)
        """
        button = QToolButton(parent)
        button.setObjectName(text)
        button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        button.setPopupMode(QToolButton.MenuButtonPopup)
        parent.addWidget(button)
        self.actions.append(button)
        return button

    @staticmethod
    def initGui():
        return True

    @staticmethod
    def unload():
        return True

    @pyqtSlot(bool, name="on_showToolbarPushButton_toggled")
    def toggleToolbar(self, toggled=None):
        """
        Shows/Hides the toolbar showAccountPushButton
        """
        if toggled is None:
            toggled = self.showToolbarPushButton.isChecked()
        if toggled:
            self.splitter.show()
        else:
            self.splitter.hide()

    @staticmethod
    def createTrialProject():
        """
        Shows the dialog that loads layers from server
        """
        dlg = GeostatisticsTrial()
        dlg.show()
        result = dlg.exec_()
        if result:
            pass

    def loadFiles(self):
        project = self.layerService.checkForSavedProject()
        if project:
            dlg = LoadFiles(project)
            dlg.show()
            result = dlg.exec_()
            if result:
                pass

    @staticmethod
    def manageLpcTeam():
        dlg = RegisterLpcTeam()
        dlg.show()
        result = dlg.exec_()
        if result:
            pass

    @staticmethod
    def manageFarmer():
        dlg = FarmerManager()
        dlg.show()
        result = dlg.exec_()
        if result:
            pass

    def treatments(self):
        project = self.layerService.checkForSavedProject()
        if project:
            dlg = TreatmentPolygons(project)
            dlg.show()
            result = dlg.exec_()
            if result:
                pass

    def filtering(self):
        project = self.layerService.checkForSavedProject()
        if project:
            dlg = FilteringPoints(self.iface, project)
            dlg.show()
            result = dlg.exec_()
            if result:
                pass

    def ordinaryKriging(self):
        project = self.layerService.checkForSavedProject()
        if project:
            dlg = OrdinaryKriging(self.iface, project)
            dlg.show()
            result = dlg.exec_()
            if result:
                pass

    def validation(self):
        project = self.layerService.checkForSavedProject()
        if project:
            dlg = SamplingValidation(self.iface, project)
            dlg.show()
            result = dlg.exec_()
            if result:
                pass

    def clearTreeView(self):
        project = self.layerService.checkForSavedProject()
        root = project.layerTreeRoot()
        if project:
            for index, layer in enumerate(self.iface.mapCanvas().layers()):
                if layer.type() == QgsMapLayer.RasterLayer:
                    layer_node = root.findLayer(layer.id())

                    if 'validation' in layer.name().split('_'):
                        self.layerService.applySymbology(layer, '', raster=True)
                        self.layerService.addMapLayer(layer, QGIS_TOC_GROUPS[5])
                    else:
                        self.layerService.applySymbology(layer, '', raster=True)
                        self.layerService.addMapLayer(layer, QGIS_TOC_GROUPS[3])

                    parent = layer_node.parent()
                    parent.removeChildNode(layer_node)

    def getReport(self):
        project = self.layerService.checkForSavedProject()
        if project:
            dlg = StatisticsReport(self.iface, project)
            dlg.show()
            result = dlg.exec_()
            if result:
                pass

    def composer(self):
        project = self.layerService.checkForSavedProject()
        if project:
            self.algRunner.runLoadComposerTemplates(project)

    def exportMaps(self):
        project = self.layerService.checkForSavedProject()
        if project:
            self.algRunner.runExportMaps(project)
