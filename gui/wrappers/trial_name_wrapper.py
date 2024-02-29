# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TrialNameWidgetWrapper
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

from processing.gui.wrappers import WidgetWrapper
from qgis.PyQt import QtWidgets
from qgis.core import (QgsProcessingParameterDefinition)

from ...core.constants import FETCH_ALL_TRIAL
from ...core.factories.postgres_factory import PostgresFactory


class TrialNameWidgetWrapper(WidgetWrapper):
    def __init__(self, *args, **kwargs):
        super(TrialNameWidgetWrapper, self).__init__(*args, **kwargs)

    def createWidget(self):
        self.trialComboBox = QtWidgets.QComboBox()
        PostgresFactory().fetchDataToCombobox(self.trialComboBox, FETCH_ALL_TRIAL, ['field_name'], 'id')
        self.trialComboBox.dialogType = self.dialogType
        return self.trialComboBox

    def parentLayerChanged(self, layer=None):
        pass

    def setLayer(self, layer):
        pass

    def setValue(self, value):
        pass

    def value(self):
        return self.trialComboBox.itemData(self.trialComboBox.currentIndex())

    def postInitialize(self, wrappers):
        pass


class ParameterTrialName(QgsProcessingParameterDefinition):
    def __init__(self, name, description=""):
        super().__init__(name, description)

    def clone(self):
        copy = ParameterTrialName(self.name(), self.description())
        return copy

    def type(self):
        return self.typeName()

    @staticmethod
    def typeName():
        return "trialname"

    def checkValueIsAcceptable(self, value, context=None):
        return True

    def metadata(self):
        return {
            "widget_wrapper": "lallemand_plant_care.gui.wrappers.trial_name_wrapper.TrialNameWidgetWrapper"
        }

    def valueAsPythonString(self, value, context):
        return str(value)

    def asScriptCode(self):
        raise NotImplementedError()

    @classmethod
    def fromScriptCode(cls, name, description, isOptional, definition):
        raise NotImplementedError()
