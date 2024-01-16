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

from qgis.PyQt.QtCore import QSettings
from qgis.PyQt.QtGui import QIcon
from qgis.gui import QgsOptionsWidgetFactory, QgsOptionsPageWidget

from ...core.constants import DEFAULT_SETTINGS
from .options_settings_dlg_base import Ui_Form

SETTINGS_KEY = "LPC/postgresConnection"


class OptionsSettingsFactory(QgsOptionsWidgetFactory):

    def __init__(self):
        super().__init__()

    def icon(self):
        return QIcon(':plugins/lallemand_plant_care/icons/lallemand.png')

    def createWidget(self, parent=None):
        return OptionsSettingsPage(parent)


class OptionsSettingsPage(QgsOptionsPageWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        self.server = DEFAULT_SETTINGS['SERVER']
        self.treatment = DEFAULT_SETTINGS['TREATMENT']
        self.kriging = DEFAULT_SETTINGS['KRIGING']
        self.loadSettings()

    def apply(self):
        self.saveSettings()

    def saveSettings(self):
        self.saveServerSettings()
        self.saveTreatmentPolygonsSettings()
        self.saveKrigingSettings()

    def loadSettings(self):
        self.loadServerSettings()
        self.loadTreatmentPolygonsSettings()
        self.loadKrigingSettings()

    def saveServerSettings(self):
        self.settings.setValue('LPC/database', self.databaseNameLineEdit.text())
        self.settings.setValue('LPC/host', self.serverIpLineEdit.text())
        self.settings.setValue('LPC/port', self.serverPortLineEdit.text())
        self.settings.setValue('LPC/user', self.serverUserLineEdit.text())
        self.settings.setValue('LPC/password', self.serverPasswordLineEdit.text())

    def loadServerSettings(self):
        self.databaseNameLineEdit.setText(self.settings.value('LPC/database', self.server[0]))
        self.serverIpLineEdit.setText(self.settings.value('LPC/host', self.server[1]))
        self.serverPortLineEdit.setText(self.settings.value('LPC/port', self.server[2]))
        self.serverUserLineEdit.setText(self.settings.value('LPC/user', self.server[3]))
        self.serverPasswordLineEdit.setText(self.settings.value('LPC/password', self.server[4]))

    def getServerSettings(self):
        return {
            'database': self.settings.value('LPC/database'),
            'host': self.settings.value('LPC/host'),
            'port': self.settings.value('LPC/port'),
            'user': self.settings.value('LPC/user'),
            'password': self.settings.value('LPC/password')
        }

    def saveTreatmentPolygonsSettings(self):
        self.settings.setValue('LPC/odd_polygons', self.oddPolygonsNameLineEdit.text())
        self.settings.setValue('LPC/even_polygons', self.evenPolygonsNameLineEdit.text())
        self.settings.setValue('LPC/largeur_coupe', self.largeurCoupeSpinBox.value())
        self.settings.setValue('LPC/sous_echantillonnage', self.sousEchantillonnageSpinBox.value())

    def loadTreatmentPolygonsSettings(self):
        self.oddPolygonsNameLineEdit.setText(self.settings.value('LPC/odd_polygons', self.treatment[0]))
        self.evenPolygonsNameLineEdit.setText(self.settings.value('LPC/even_polygons', self.treatment[1]))
        self.largeurCoupeSpinBox.setValue(float(self.settings.value('LPC/largeur_coupe', self.treatment[2])))
        self.sousEchantillonnageSpinBox.setValue(float(self.settings.value('LPC/sous_echantillonnage', self.treatment[3])))

    def getTreatmentPolygonsSettings(self):
        return (
            self.settings.value('LPC/odd_polygons'),
            self.settings.value('LPC/even_polygons'),
            self.settings.value('LPC/largeur_coupe'),
            self.settings.value('LPC/sous_echantillonnage')
        )

    def saveKrigingSettings(self):
        self.settings.setValue('LPC/field_interpolate', self.fieldToInterpolateLineEdit.text())
        self.settings.setValue('LPC/pixel_size_x', self.pixelSizeXSpinBox.value())
        self.settings.setValue('LPC/pixel_size_y', self.pixelSizeYSpinBox.value())


    def loadKrigingSettings(self):
        self.fieldToInterpolateLineEdit.setText(self.settings.value('LPC/field_interpolate', self.kriging[0]))
        self.pixelSizeXSpinBox.setValue(float(self.settings.value('LPC/pixel_size_x', self.kriging[1])))
        self.pixelSizeYSpinBox.setValue(float(self.settings.value('LPC/pixel_size_y', self.kriging[2])))

    def getKrigingSettings(self):
        fields = self.settings.value('LPC/field_interpolate').split(';')
        pixelSize = [self.settings.value('LPC/pixel_size_x'), self.settings.value('LPC/pixel_size_y')]
        return fields, pixelSize
