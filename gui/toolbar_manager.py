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

from qgis.PyQt.QtCore import pyqtSlot
from qgis.PyQt.QtWidgets import QWidget

from .filter.filtering_dlg import FilteringPoints
from .kriging.kriging_dlg import OrdinaryKriging
from .treatment.treatment_polygons_dlg import TreatmentPolygons
from .geostatistics_trial.geostatistics_trial import GeostatisticsTrial
from .layer_manager.load_files_dlg import LoadFiles
from .lpc_team.farmer_manager import FarmerManager
from .lpc_team.lpc_team_manager import RegisterLpcTeam
from .toolbar.toolbar_form_base import Ui_Form
from ..core.services.layer_service import LayerService


class ToolbarManager(QWidget, Ui_Form):
    def __init__(self, iface, toolbar=None):
        """Constructor."""
        super(ToolbarManager, self).__init__()
        self.setupUi(self)
        self.iface = iface
        self.toolbar = toolbar
        self.layerService = LayerService()
        self.splitter.hide()
        self.settingsPushButton.hide()
        self.reportPushButton.hide()
        self.createTrialPushButton.clicked.connect(self.createTrialProject)
        self.loadFilePushButton.clicked.connect(self.loadFiles)
        self.lpcTeamPushButton.clicked.connect(self.manageLpcTeam)
        self.farmerPushButton.clicked.connect(self.manageFarmer)
        self.treatmentPushButton.clicked.connect(self.treatments)
        self.filterPushButton.clicked.connect(self.filtering)
        self.krigingPushButton.clicked.connect(self.ordinaryKriging)

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
