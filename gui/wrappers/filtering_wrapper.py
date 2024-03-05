# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FilteringWidgetWrapper
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
from qgis.core import (QgsProject, QgsMapLayerProxyModel, QgsProcessingParameterDefinition)
from qgsmaplayercombobox import QgsMapLayerComboBox

from ...core.services.layer_service import LayerService


class FilteringWidgetWrapper(WidgetWrapper):
    def __init__(self, *args, **kwargs):
        super(FilteringWidgetWrapper, self).__init__(*args, **kwargs)

    def createWidget(self):
        layerService = LayerService()
        self.layerComboBox = QgsMapLayerComboBox()
        layers = QgsProject.instance().mapLayers()
        treatmentLayer = layerService.filterByLayerName(list(layers.values()), ['1_Krig_', 'GPS', 'T1', 'T2', 'Gain', 'Yield'], inverse=True)

        self.layerComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.layerComboBox.setExceptedLayerList(treatmentLayer)
        return self.layerComboBox

    def parentLayerChanged(self, layer=None):
        pass

    def setLayer(self, layer):
        self.layerComboBox.setLayer(layer)

    def setValue(self, value):
        pass

    def value(self):
        return self.layerComboBox.currentLayer()

    def postInitialize(self, wrappers):
        pass


class ParameterFiltering(QgsProcessingParameterDefinition):
    def __init__(self, name, description="", optional=False):
        super().__init__(name, description, optional)

    def clone(self):
        copy = ParameterFiltering(self.name(), self.description())
        return copy

    def type(self):
        return self.typeName()

    @staticmethod
    def typeName():
        return "filteredlayer"

    def checkValueIsAcceptable(self, value, context=None):
        return True

    def metadata(self):
        return {
            "widget_wrapper": "lallemand_plant_care.gui.wrappers.filtering_wrapper.FilteringWidgetWrapper"
        }

    def valueAsPythonString(self, value, context):
        return str(value)

    def asScriptCode(self):
        raise NotImplementedError()

    @classmethod
    def fromScriptCode(cls, name, description, isOptional, definition):
        raise NotImplementedError()
