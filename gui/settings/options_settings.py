# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PostgresFactory
                                 A QGIS plugin
 Lallemand Plant Care
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
import json
import os

from qgis.PyQt import uic
from qgis.PyQt.QtCore import QSettings
from qgis.PyQt.QtGui import QIcon
from qgis.gui import QgsOptionsWidgetFactory, QgsOptionsPageWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'options_settings.ui'))

SETTINGS_KEY = "LPC/postgresConnection"


class OptionsSettingsFactory(QgsOptionsWidgetFactory):

    def __init__(self):
        super().__init__()

    def icon(self):
        return QIcon(':plugins/lallemand_plant_care/icons/lallemand.png')

    def createWidget(self, parent=None):
        return OptionsSettingsPage(parent)


class OptionsSettingsPage(QgsOptionsPageWidget, FORM_CLASS):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.loadSettings()

    def apply(self):
        self.saveSettings()

    def saveSettings(self):
        settings = QSettings()

        settings.setValue('LPC/database', self.databaseNameLineEdit.text())
        settings.setValue('LPC/host', self.serverIpLineEdit.text())
        settings.setValue('LPC/port', self.serverPortLineEdit.text())
        settings.setValue('LPC/user', self.serverUserLineEdit.text())
        settings.setValue('LPC/password', self.serverPasswordLineEdit.text())

    def loadSettings(self):
        settings = QSettings()

        self.databaseNameLineEdit.setText(settings.value('LPC/database'))
        self.serverIpLineEdit.setText(settings.value('LPC/host'))
        self.serverPortLineEdit.setText(settings.value('LPC/port'))
        self.serverUserLineEdit.setText(settings.value('LPC/user'))
        self.serverPasswordLineEdit.setText(settings.value('LPC/password'))

        return {
            'database': settings.value('LPC/database'),
            'host': settings.value('LPC/server'),
            'port': settings.value('LPC/port'),
            'user': settings.value('LPC/user'),
            'password': settings.value('LPC/password')
        }
