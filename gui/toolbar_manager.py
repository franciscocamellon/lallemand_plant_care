# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GuiManager
                                 A QGIS plugin
 Lallemand - Crop Analysis Environment
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

from __future__ import absolute_import
from builtins import object
import os.path
import sys

from qgis.PyQt.QtCore import QObject, Qt, pyqtSignal, pyqtSlot
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QToolButton, QMenu, QAction, QWidget

from .crop_analysis_environment_ui import CropAnalysisEnvironmentUi
from .layer_manager.create_project import CreateProject
from .layer_manager.load_files import LoadFiles
from .toolbar_ui import Ui_Form


class ToolbarManager(QWidget, Ui_Form):
    def __init__(self, iface, project, toolbar=None):
        """Constructor.
        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        super(ToolbarManager, self).__init__()
        self.setupUi(self)
        self.iface = iface
        self.project = project
        self.icon_base_path = ":/plugins/crop_analysis_environment/icons/"
        self.actions = []
        self.managerList = []
        self.menuList = []
        self.toolbar = toolbar
        self.splitter.hide()
        self.create_project_pb.clicked.connect(self.create_project)
        self.load_file_pb.clicked.connect(self.load_files)

    def create_tool_button(self, parent, text):
        """
        Creates a tool button (pop up menu)
        """
        button = QToolButton()
        button.setObjectName(text)
        button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        button.setPopupMode(QToolButton.MenuButtonPopup)
        parent.addWidget(button)
        self.actions.append(button)
        return button

    def instantiateManagers(self):

        pass

    def initGui(self):
        return True

    def unload(self):
        return True

    @pyqtSlot(bool, name="on_show_toolbar_pb_toggled")
    def toggleBar(self, toggled=None):
        """
        Shows/Hides the tool bar
        """
        if toggled is None:
            toggled = self.show_toolbar_pb.isChecked()
        if toggled:
            self.splitter.show()
        else:
            self.splitter.hide()

    def create_project(self):
        """
        Shows the dialog that loads layers from server
        """
        # dlg = CreateProject(self.iface, self.project)
        dlg = CropAnalysisEnvironmentUi(self.iface, self.project)
        dlg.show()
        result = dlg.exec_()
        if result:
            pass
    def load_files(self):
        """
        Shows the dialog that loads layers from server
        """
        dlg = LoadFiles(self.iface, self.project)
        dlg.show()
        result = dlg.exec_()
        if result:
            pass