# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CropAnalysisEnvironmentDialog
                                 A QGIS plugin
 Lallemand - Crop Analysis Environment
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-10-04
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

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets, uic

from .crop_analysis_environment_ui_form import Ui_CropAnalysisEnvironmentForm
from ..services.layer_service import LayerService


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
# FORM_CLASS, _ = uic.loadUiType(os.path.join(
#     os.path.dirname(__file__), 'crop_analysis_environment_ui.ui'))


class CropAnalysisEnvironmentUi(QtWidgets.QDialog, Ui_CropAnalysisEnvironmentForm):
    def __init__(self, iface, project, parent=None):
        """Constructor."""
        super(CropAnalysisEnvironmentUi, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface
        self.project = project
        self.layer_services = LayerService(self.iface)
        self.createTrialBt.clicked.connect(self.saveQgisProject)
        self.cancelTrialBt.clicked.connect(self.load_shape_file)

    def saveQgisProject(self):
        self.project.setCrs(self.trialQgisProjectCrs.crs())
        self.project.write(f'{self.trialDirectory.filePath()}/{self.trialQgisProjectName.text()}.qgs')

    def load_shape_file(self):
        group_name = self.retrieve_group_name(self.harvester_rb.isChecked(), self.gps_rb.isChecked())
        self.layer_services.load_shape_file(self.project, group_name, self.load_file_fw.filePath())

    @staticmethod
    def retrieve_group_name(harvester, gps):
        if harvester:
            return 'Harvester points'
        elif harvester is False and gps is False:
            return None
        else:
            return 'GPS points'
