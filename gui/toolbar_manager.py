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

from qgis.PyQt.QtCore import pyqtSlot
from qgis.PyQt.QtWidgets import QWidget

from core.tools.load_files import LoadFiles
from .toolbar.ui_toolbar_manager import Ui_Form
from ..core.tools.geostatistics_trial import GeostatisticsTrial


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
        self.toolbar = toolbar
        self.splitter.hide()
        self.createTrialPushButton.clicked.connect(self.createTrialProject)
        self.loadFilePushButton.clicked.connect(self.loadFiles)

    @staticmethod
    def initGui():
        return True

    @staticmethod
    def unload():
        return True

    @pyqtSlot(bool, name="on_showToolbarPushButton_toggled")
    def toggleBar(self, toggled=None):
        """
        Shows/Hides the toolbar
        """
        if toggled is None:
            toggled = self.showToolbarPushButton.isChecked()
        if toggled:
            self.splitter.show()
        else:
            self.splitter.hide()

    def createTrialProject(self):
        """
        Shows the dialog that loads layers from server
        """
        dlg = GeostatisticsTrial(self.iface, self.project)
        dlg.show()
        result = dlg.exec_()
        if result:
            pass

    def loadFiles(self):
        """
        Shows the dialog that loads layers from server
        """
        dlg = LoadFiles(self.iface, self.project)
        dlg.show()
        result = dlg.exec_()
        if result:
            pass
