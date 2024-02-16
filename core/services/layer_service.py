# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LayerService
                                 A QGIS plugin
 Lallemand Plant Care
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-09-28
        git sha              : $Format:%H$
        copyright            : (C) 2023 by ETG
        email                : etg@email.com
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
import random
import re
from contextlib import contextmanager

from qgis.core import (
    QgsProject,
    QgsField,
    QgsFields,
    QgsVectorLayer,
    QgsRasterLayer,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsLayerTreeGroup,
    QgsLayerTreeLayer,
    QgsCoordinateTransform,
    QgsVectorFileWriter,
    QgsCoordinateTransformContext,
    QgsWkbTypes,
    QgsFeatureRequest,
    QgsExpression,
    QgsGraduatedSymbolRenderer,
    QgsRendererRange,
    QgsMarkerSymbol, QgsLegendRenderer,
    QgsLegendStyle,
)
from qgis.PyQt.QtWidgets import QMessageBox, QFileDialog
from qgis.PyQt.Qt import QVariant
from qgis.PyQt.QtGui import QColor

from .plot_service import PlotterService
from ...gui.settings.options_settings_dlg import OptionsSettingsPage
from .message_service import MessageService
from .system_service import SystemService
from ..constants import VALIDATION_FIELDS
from ..tools.algorithm_runner import AlgorithmRunner


class LayerService:

    def __init__(self, default_crs=None):
        self.default_crs = default_crs
        self.project = QgsProject.instance()
        self.messageService = MessageService()
        self.systemService = SystemService()
        self.plotterService = PlotterService()
        self.settings = OptionsSettingsPage()
        self.krigingSettings = self.settings.getKrigingSettings()

    @staticmethod
    def _identifyWkbType(layer):
        convertedLayerType = ''
        if layer.geometryType() == QgsWkbTypes.PointZ:
            convertedLayerType = "Point"
        elif layer.geometryType() == QgsWkbTypes.LineStringZ:
            convertedLayerType = "LineString"
        elif layer.geometryType() == QgsWkbTypes.PolygonZ:
            convertedLayerType = "Polygon"
        return convertedLayerType

    @staticmethod
    def _getWorldZonesPath():
        currentDirectory = os.path.dirname(__file__)
        parentDirectory = os.path.join(currentDirectory, '..')
        return os.path.join(parentDirectory, 'resources', 'world_zones.geojson')

    @staticmethod
    def getComposerLayoutPath():
        currentDirectory = os.path.dirname(__file__)
        parentDirectory = os.path.join(currentDirectory, '..')
        return os.path.join(parentDirectory, 'resources', 'composer')

    def listQptFiles(self):
        directoryPath = self.getComposerLayoutPath()
        return [os.path.join(directoryPath, file) for file in os.listdir(directoryPath) if file.endswith('.qpt')]

    @staticmethod
    def getReportPath():
        currentDirectory = os.path.dirname(__file__)
        parentDirectory = os.path.join(currentDirectory, '..')
        return os.path.join(parentDirectory, 'resources', 'report')

    @staticmethod
    def getPresentationPath():
        currentDirectory = os.path.dirname(__file__)
        parentDirectory = os.path.join(currentDirectory, '..')
        return os.path.join(parentDirectory, 'resources', 'presentation')

    @staticmethod
    def _getGeometryFromWkbType(wkbType):
        return QgsWkbTypes.displayString(wkbType)

    @staticmethod
    def checkLayerGeometry(layer):
        return True if layer.geometryType() in [1, 2, 3] else False

    @staticmethod
    def addLayerToTreeGroup(project, layer, groupName):
        root = project.instance().layerTreeRoot()
        group = root.findGroup(groupName)
        group.addLayer(layer)

    @staticmethod
    def addMapLayer(layer, groupName):
        project = QgsProject.instance()
        root = project.instance().layerTreeRoot()
        group = root.findGroup(groupName)

        if group is not None:
            project.instance().addMapLayer(layer, False)
            group.addLayer(layer)

        else:
            group = QgsLayerTreeGroup(groupName)
            root.addChildNode(group)
            project.instance().addMapLayer(layer, False)
            group.addLayer(layer)

    def krigingFilterLayerByName(self, layers, filterString, inverse=False):
        krigingLayers = []

        for layer in layers:
            if not layer.crs().isGeographic():
                krigingLayers.append(layer)

        return self.filterByLayerName(krigingLayers, filterString, inverse=inverse)

    @staticmethod
    def filterByLayerName(layers, filterString, inverse=False):
        filteredLayers = []
        regexPattern = '|'.join(map(re.escape, filterString))
        pattern = re.compile(regexPattern)

        for layer in layers:
            if inverse and pattern.search(layer.name()):
                filteredLayers.append(layer)
            elif not inverse and not pattern.search(layer.name()):
                filteredLayers.append(layer)

        return filteredLayers

    @staticmethod
    def filterByFieldName(layer, filterString, inverse=False):
        filteredFields = QgsFields()
        regexPattern = '|'.join(map(re.escape, filterString))
        pattern = re.compile(regexPattern)

        if layer:
            for field in layer.fields():
                if inverse and not pattern.search(field.name()):
                    filteredFields.append(field)
                elif not inverse and pattern.search(field.name()):
                    filteredFields.append(field)

        return filteredFields

    @staticmethod
    def _getFieldsDictionary(layer):
        fieldsDictionary = {}
        fields = layer.fields()
        for field in fields:
            fieldsDictionary[fields.lookupField(field.name())] = field.name()
        return fieldsDictionary

    @staticmethod
    def getFeaturesByRequest(layer, expression):
        request = QgsExpression(expression)
        return layer.getFeatures(QgsFeatureRequest(request))

    @staticmethod
    def getPercentualFeaturesById(layer, value):
        ids = layer.allFeatureIds()
        value = int(round(value / 100.0, 4) * len(ids))
        randomSelection = random.sample(ids, value)

        layer.selectByIds(randomSelection)

        return layer.getSelectedFeatures()

    @staticmethod
    def _createQgsField(fieldName, fieldType):
        return QgsField(fieldName, fieldType)

    # @contextmanager
    # def safe_file_operations(self, file_path, mode='r'):
    #     """Context manager for safe file operations."""
    #     file = None
    #     try:
    #         file = open(file_path, mode)
    #         yield file
    #     finally:
    #         if file:
    #             file.close()

    @staticmethod
    def getValuesByExpression(layer, expression, field):
        expr = QgsExpression(expression)
        request = QgsFeatureRequest(expr)
        features = layer.getFeatures(request)
        return [feature[field] for feature in features]

    def populateFrequencyHistogram(self, layer, field, data, path):
        histogramValues = [feature[field] for feature in layer.getFeatures()]
        self.plotterService.createFrequencyHistogram(histogramValues, data, layer.name(), exportPng=True, path=path)

    def filterFeaturesByIntervals(self, layer):
        totalFeatures = [feature['yield'] for feature in layer.getFeatures()]
        firstInterval = self.getValuesByExpression(layer, '"yield" < 0', 'yield')
        secondInterval = self.getValuesByExpression(layer, '0 <= "yield" AND "yield" < 0.5', 'yield')
        thirdInterval = self.getValuesByExpression(layer, '0.5 <= "yield" AND "yield" < 1', 'yield')
        fourthInterval = self.getValuesByExpression(layer, '"yield" >= 1', 'yield')
        total = len(totalFeatures)
        values = [firstInterval, secondInterval, thirdInterval, fourthInterval]
        return total, values

    @staticmethod
    def getPercentualFromIntervals(total, listOfIntervals, string=False):
        if string:
            return [f'{(len(interval) / total) * 100:.2f}%' for interval in listOfIntervals]
        return [(len(interval) / total) * 100 for interval in listOfIntervals]

    def yieldGainFrequencyHistogram(self, layer, path):

        total, values = self.filterFeaturesByIntervals(layer)

        if total != 0:
            percentages = self.getPercentualFromIntervals(total, values, True)
            self.plotterService.yieldFrequencyHistogram(values, percentages, exportPng=True, path=path)

    def _convertToSimpleGeometry(self, layer):
        convertedLayerType = self._identifyWkbType(layer)
        convertedLayer = QgsVectorLayer(f"{convertedLayerType}?crs={layer.crs().authid()}", layer.name(), "memory")

        for feature in layer.getFeatures():
            convertedFeature = QgsFeature(layer.fields())
            convertedFeature.setGeometry(QgsWkbTypes.dropZ(feature.geometry().wkbType()))
            convertedLayer.dataProvider().addFeature(convertedFeature)

        return convertedLayer

    def createValidationFields(self, layer):

        fields = [self._createQgsField(fieldName, QVariant.Double) for fieldName in VALIDATION_FIELDS]
        provider = layer.dataProvider()
        provider.addAttributes(fields)
        layer.updateFields()

        return layer

    def deleteFields(self, layer, fields):
        fieldsDictionary = self._getFieldsDictionary(layer)
        provider = layer.dataProvider()
        fieldsToDelete = []

        for index, fieldName in fieldsDictionary.items():
            for field in fields:
                if field.name() == fieldName:
                    fieldsToDelete.append(index)

        provider.deleteAttributes(fieldsToDelete)
        layer.updateFields()

        return layer

    def createValidationVectorLayer(self, layer):
        # TODO with edit(layer):
        fields = self.krigingSettings[0]
        fields.append('1Krig')
        fields.append('fid')
        fieldsToDelete = self.filterByFieldName(layer, fields, inverse=True)
        newOutput = self.deleteFields(layer, fieldsToDelete)
        return self.createValidationFields(newOutput)

    def checkForSavedProject(self):

        if self.project.fileName():

            projectPath = self.project.homePath()
            self.systemService.createDirectoryStructure(projectPath)

            return self.project

        else:
            choice = self.messageService.standardButtonMessage('Load trial files',
                                                               ['There is no saved QGIS project.',
                                                                'Do you want to save your project now?'],
                                                               3, [5, 6])
            if choice == 16384:
                fileDialog = self.messageService.saveFileDialog()

                if fileDialog.exec_():
                    filePath = fileDialog.selectedFiles()[0]
                    self.project.write(filePath)

                    self.systemService.createDirectoryStructure(self.project.homePath())

                    return self.project
            else:
                self.messageService.warningMessage("Project Save", "Project not saved.")
                return None

    def loadShapeFile(self, groupName, file_path):

        try:
            fileName = self.systemService.extractFileName(file_path)
            layer = self.createVectorLayer(fileName, file_path)

            if groupName is None:
                self.project.addMapLayer(layer)
            else:
                root = self.project.instance().layerTreeRoot()
                group = root.findGroup(groupName)

                if group:
                    self.project.addMapLayer(layer, False)
                    group.addLayer(layer)
                else:
                    self.project.addMapLayer(layer, False)
                    root = self.createLayerTreeGroup(self.project, groupName)
                    group = root.findGroup(groupName)
                    group.addLayer(layer)

            return layer

        except Exception as load_file_exception:
            errorMessage = f'Error loading shape file: {str(load_file_exception)}'
            self.messageService.messageBox('Loading file', errorMessage, 5, 1)

    def createMemoryVectorLayer(self, wkbType, layerName, crs, fields=None, features=None):
        geometry = self._getGeometryFromWkbType(wkbType)
        uri = f'{geometry}?crs={crs}&index=yes'

        try:
            layer = QgsVectorLayer(uri, layerName, "memory")
            provider = layer.dataProvider()

            if fields is not None:
                provider.addAttributes(fields)
                layer.updateFields()

            if features is not None:
                provider.addFeatures(features)
                layer.updateExtents()

            if not layer.isValid():
                raise Exception('Layer is not valid.')

            return layer

        except Exception as createLayerException:
            errorMessage = f'Error creating layer {layerName} -> {str(createLayerException)}'
            self.messageService.messageBox('Loading file', errorMessage, 5, 1)
            return None

    def createVectorLayer(self, layerName, filePath, useDefaultCrs=True):

        try:
            if useDefaultCrs:
                crs = self.default_crs
            else:
                crs = None

            layer = QgsVectorLayer(filePath, layerName, "ogr")

            if not layer.isValid():
                raise Exception('Layer is not valid.')

            if crs is not None:
                layer.setCrs(crs)

            return layer

        except Exception as createLayerException:
            errorMessage = f'Error creating layer {layerName} -> {str(createLayerException)}'
            self.messageService.messageBox('Loading file', errorMessage, 5, 1)
            return None

    def convertFeatureCrs(self, layer, target_crs, feedback=None):
        transformedLayer = self.createMemoryVectorLayer(layer.wkbType(), layer.name(), target_crs,
                                                        fields=layer.fields())
        provider = transformedLayer.dataProvider()
        try:
            if not layer.isValid():
                raise Exception('Invalid layer for CRS conversion.')

            if target_crs is None:
                raise Exception('Target CRS is not specified.')

            source_crs = layer.crs()
            transform_context = QgsCoordinateTransform.Context()
            transform = QgsCoordinateTransform(source_crs, target_crs, transform_context)

            transformedFeature = []
            for idx, feature in enumerate(layer.getFeatures()):
                geometry = feature.geometry()
                if not geometry.isEmpty():
                    geometry.transform(transform)
                    feature.setGeometry(geometry)
                    transformedFeature.append(feature)
                    feedback.setProgress(idx)
            provider.addFeatures(transformedFeature)
            transformedLayer.updateExtents()

            return transformedLayer

        except Exception as e:
            errorMessage = f'Error converting layer CRS: {str(e)}'
            self.messageService.messageBox('Loading file', errorMessage, 5, 1)
            return False

    def createLayerTreeGroup(self, qgs_project, group_name):

        try:
            root = qgs_project.instance().layerTreeRoot()
            group = QgsLayerTreeGroup(group_name)
            root.addChildNode(group)
            return root

        except Exception as group_exception:
            errorMessage = f'Error creating layer tree group: {str(group_exception)}'
            self.messageService.messageBox('Loading file', errorMessage, 5, 1)
            return None

    def getSuggestedCrs(self, layer):

        worldZoneFileDirectory = self._getWorldZonesPath()
        zoneFile = self.createVectorLayer('world_zones', worldZoneFileDirectory)

        if not layer.isValid():
            print('Layer not valid!')
        else:

            layer_extent = layer.extent()
            bounding_box_polygon = QgsGeometry.fromRect(layer_extent)
            centroid = bounding_box_polygon.centroid().asPoint()

            for feature in zoneFile.getFeatures():
                polygon_geometry = feature.geometry()

                if polygon_geometry.contains(centroid):
                    return feature.attributes()
            else:
                print('Centroid is not within any polygon in world zones layer')

    def saveVectorLayer(self, layer, outputPath):
        writerOptions = QgsVectorFileWriter.SaveVectorOptions()
        writerOptions.fileEncoding = 'UTF-8'
        writerOptions.driverName = 'ESRI Shapefile'

        try:

            error, errorMessage, layerPath, layerName = QgsVectorFileWriter.writeAsVectorFormatV3(
                layer,
                outputPath,
                QgsCoordinateTransformContext(),
                options=writerOptions
            )

            if error == QgsVectorFileWriter.NoError:
                # self.messageService.informationMessage('Saving file', f'Layer saved successfully to {outputPath}')
                pass

        except Exception as e:
            self.messageService.criticalMessage('Saving file', f'An error occurred: {str(e)}')

    def getLoadedVectorLayers(self, layers, geographic=False):
        vectorLayers = []
        for layer in layers:
            if geographic:
                if isinstance(layer, QgsVectorLayer) and layer.crs().isGeographic():
                    vectorLayers.append(layer)
            else:
                if isinstance(layer, QgsVectorLayer) and not layer.crs().isGeographic():
                    vectorLayers.append(layer)
        return vectorLayers

    def getLoadedRasterLayers(self, layers):
        return [layer for layer in layers if isinstance(layer, QgsRasterLayer)]

    @staticmethod
    def extractValueFromRaster(raster, feature, fieldName):
        """
        Extracts a value from a raster at the location of a feature's geometry point.
        :param raster: The raster layer from which to extract the value.
        :param feature: The feature for which the value is extracted.
        :param fieldName: The name of the field where the extracted value will be stored.
        :returns: The updated feature with the extracted value.
        """
        geometry = feature.geometry()
        observation_point = geometry.asPoint()
        x, y = observation_point.x(), observation_point.y()

        pixel_value, success = raster.dataProvider().sample(QgsPointXY(x, y), 1)

        if success:
            feature[fieldName] = pixel_value

        return feature

    def createLayerSymbology(self, layer, fieldName):
        minValue = layer.minimumValue(layer.fields().indexOf(fieldName))
        maxValue = layer.maximumValue(layer.fields().indexOf(fieldName))

        step = (maxValue - minValue) / 4
        adjustedIntervals = [round((maxValue - i * step), 1) for i in range(5)]

        colors = ['#267300', '#55ff00', '#ffff00', '#bfbcbc']

        ranges = []
        for i in range(4):
            symbol = QgsMarkerSymbol.createSimple({'size': '1.5'})
            symbol.setColor(QColor(colors[i]))

            if i == 0:
                label = f"> {adjustedIntervals[i + 1]}"
            elif i == 3:
                label = f"< {adjustedIntervals[i]}"
            else:
                label = f"{adjustedIntervals[i + 1]} - {adjustedIntervals[i]}"

            intervalRange = QgsRendererRange(adjustedIntervals[i + 1], adjustedIntervals[i], symbol, label)
            ranges.append(intervalRange)

        renderer = QgsGraduatedSymbolRenderer(fieldName, ranges)
        renderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)

        return renderer

    def applySymbology(self, layer, fieldName):
        renderer = self.createLayerSymbology(layer, fieldName)
        layer.setRenderer(renderer)
        layer.triggerRepaint()
