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
import math
import os
import random
import re

from qgis.PyQt.Qt import QVariant
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QColor
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
    QgsCoordinateTransform,
    QgsVectorFileWriter,
    QgsCoordinateTransformContext,
    QgsWkbTypes,
    QgsFeatureRequest,
    QgsExpression,
    QgsGraduatedSymbolRenderer,
    QgsColorRampShader,
    QgsRasterShader,
    QgsColorRampLegendNodeSettings,
    QgsSingleBandPseudoColorRenderer,
    QgsRasterBandStats,
    QgsRendererRange,
    QgsSymbol)
from qgis.core.additions.edit import edit

from .message_service import MessageService
from .plot_service import PlotterService
from .system_service import SystemService
from ..constants import VALIDATION_FIELDS, QGIS_TOC_GROUPS
from ...gui.settings.options_settings_dlg import OptionsSettingsPage


class LayerService:

    def __init__(self, default_crs=None):
        self.default_crs = default_crs
        self.project = QgsProject.instance()
        self.messageService = MessageService()
        self.systemService = SystemService()
        self.plotterService = PlotterService()
        self.settings = OptionsSettingsPage()
        self.krigingSettings = self.settings.getKrigingSettings()
        self.symbologySettings = self.settings.getSymbologySettings()

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
    def getSqlitePath():
        currentDirectory = os.path.dirname(__file__)
        parentDirectory = os.path.join(currentDirectory, '..')
        return os.path.join(parentDirectory, 'resources', 'BD_GEOSTAT_LPC.sqlite')

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

    def createLayersTreeGroup(self, project):
        for groupName in QGIS_TOC_GROUPS:
            self.createLayerTreeGroup(project, groupName)

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
    def filterExactLayerName(layers, filterString, inverse=False):
        filteredLayers = []
        regexPattern = '|'.join(rf'\b{re.escape(s)}\b' for s in filterString)
        pattern = re.compile(regexPattern)

        for layer in layers:
            if inverse and pattern.search(layer.name()):
                filteredLayers.append(layer)
            elif not inverse and not pattern.search(layer.name()):
                filteredLayers.append(layer)

        return filteredLayers

    def filterVectorLayerByName(self, layers, filterString, inverse=False):
        filteredLayers = self.filterExactLayerName(layers, filterString, inverse=inverse)

        for layer in filteredLayers:
            if layer.type() == 0:
                return layer

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
    def getFeaturesByRequest(layer, expression, featureList=False):
        request = QgsExpression(expression)
        if featureList:
            return [feature for feature in layer.getFeatures(QgsFeatureRequest(request))]
        else:
            return layer.getFeatures(QgsFeatureRequest(request))

    @staticmethod
    def getPercentualFeaturesById(layer, value, featureList=False):
        idsList = layer.allFeatureIds()
        totalFeatures = len(idsList)
        selectedCount = int(round(value / 100.0, 4) * totalFeatures)
        randomSelection = random.sample(idsList, selectedCount)

        layer.selectByIds(randomSelection)
        if featureList:
            selectedFeatures = [feature for feature in layer.getSelectedFeatures()]
            layer.invertSelection()
            complementaryFeatures = [feature for feature in layer.getSelectedFeatures()]
        else:
            selectedFeatures = layer.getSelectedFeatures()
            layer.invertSelection()
            complementaryFeatures = layer.getSelectedFeatures()

        return selectedFeatures, complementaryFeatures

    @staticmethod
    def _createQgsField(fieldName, fieldType):
        return QgsField(fieldName, fieldType)

    @staticmethod
    def getValuesByExpression(layer, expression, field):
        expr = QgsExpression(expression)
        request = QgsFeatureRequest(expr)
        features = layer.getFeatures(request)
        return [feature[field] for feature in features]

    def populateFrequencyHistogram(self, layer, field, data, path):
        histogramValues = [feature[field] for feature in layer.getFeatures()]
        self.plotterService.createFrequencyHistogram(histogramValues, data, layer.name(), exportPng=True, path=path)
        self.plotterService.createVFrequencyHistogram(histogramValues, data, layer.name(), exportPng=True, path=path)

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
        fieldsList = fields.split(';')
        fieldsList.append('1Krig')
        fieldsList.append('fid')
        fieldsToDelete = self.filterByFieldName(layer, fieldsList, inverse=True)
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
                self.messageService.logMessage(f'Checking for saved project: Project not saved. FAILED', 2)
                return False

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
            # self.messageService.messageBox('Loading file', errorMessage, 5, 1)
            self.messageService.logMessage(f'Loading shapefile: {errorMessage}: FAILED', 2)

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
                self.messageService.logMessage(f'Creating memory layer: Layer is not valid!: FAILED', 2)
                raise Exception('Layer is not valid.')

            return layer

        except Exception as createLayerException:
            errorMessage = f'Error creating layer {layerName} -> {str(createLayerException)}'
            self.messageService.messageBox('Loading file', errorMessage, 5, 1)
            self.messageService.logMessage(f'Creating memory layer: {errorMessage}: FAILED', 2)
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
            self.messageService.logMessage(f'Creating vector layer: {errorMessage}: FAILED', 2)
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
            self.messageService.logMessage(f'Converting feature CRS: {errorMessage}: FAILED', 2)
            return False

    def createLayerTreeGroup(self, project, groupName):

        try:
            root = project.instance().layerTreeRoot()
            group = root.findGroup(groupName)

            if group is None:
                group = QgsLayerTreeGroup(groupName)
                root.addChildNode(group)
                return root
            else:
                return root

        except Exception as group_exception:
            errorMessage = f'Error creating layer tree group: {str(group_exception)}'
            self.messageService.messageBox('Loading file', errorMessage, 5, 1)
            self.messageService.logMessage(f'Creating layer group: {errorMessage}: FAILED', 2)
            return None

    def getSuggestedCrs(self, layer):

        worldZoneFileDirectory = self._getWorldZonesPath()
        zoneFile = self.createVectorLayer('world_zones', worldZoneFileDirectory)

        if not layer.isValid():
            self.messageService.logMessage(f'getSuggestedCrs: Layer not valid!: FAILED', 2)
        else:

            layer_extent = layer.extent()
            bounding_box_polygon = QgsGeometry.fromRect(layer_extent)
            centroid = bounding_box_polygon.centroid().asPoint()

            for feature in zoneFile.getFeatures():
                polygon_geometry = feature.geometry()

                if polygon_geometry.contains(centroid):
                    return feature.attributes()
            else:
                errorMsg = 'Centroid is not within any polygon in world zones layer'
                self.messageService.logMessage(f'getSuggestedCrs: {errorMsg}: FAILED', 2)

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
                pass

        except Exception as layerException:
            self.messageService.criticalMessage('Saving file', f'An error occurred: {str(layerException)}')
            self.messageService.logMessage(f'saveVectorLayer: {str(layerException)}: FAILED', 2)

    @staticmethod
    def getLoadedVectorLayers(layers, geographic=False):
        vectorLayers = []
        for layer in layers:
            if geographic:
                if isinstance(layer, QgsVectorLayer) and layer.crs().isGeographic():
                    vectorLayers.append(layer)
            else:
                if isinstance(layer, QgsVectorLayer) and not layer.crs().isGeographic():
                    vectorLayers.append(layer)
        return vectorLayers

    @staticmethod
    def getLoadedRasterLayers(layers):
        return [layer for layer in layers if isinstance(layer, QgsRasterLayer)]

    @staticmethod
    def extractValueFromRaster(raster, feature, fieldName):
        geometry = feature.geometry()
        observation_point = geometry.asPoint()
        x, y = observation_point.x(), observation_point.y()

        pixel_value, success = raster.dataProvider().sample(QgsPointXY(x, y), 1)

        if success:
            feature[fieldName] = pixel_value

        return feature

    def createSamplingLayerSymbology(self, layer, fieldName):
        minValue = layer.minimumValue(layer.fields().indexOf(fieldName))
        maxValue = layer.maximumValue(layer.fields().indexOf(fieldName))

        numberClasses = int(self.symbologySettings[0])
        classes = self.calculateVectorClasses(minValue, maxValue, numberClasses)
        colors = self.symbologySettings[1]
        colors.reverse()

        rendererInterval = list()
        for index in range(4):
            symbol = self.createSamplingPointSymbol(layer.geometryType(), colors[index], 1.5, Qt.PenStyle(Qt.NoPen))
            label = self.createClassLabels(index, classes)
            intervalRange = QgsRendererRange(classes[index + 1], classes[index], symbol, label)
            rendererInterval.append(intervalRange)

        renderer = QgsGraduatedSymbolRenderer(fieldName, rendererInterval)
        renderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
        colors.reverse()
        return renderer

    def createBoundaryLayerSymbology(self, layer):
        symbol = self.createFillSymbol(layer.geometryType(), 'black', 0.3, Qt.BrushStyle.NoBrush)
        layer.renderer().setSymbol(symbol)
        layer.triggerRepaint()

    @staticmethod
    def createFillSymbol(geometryType, color, size, brushStyle):
        symbol = QgsSymbol.defaultSymbol(geometryType)
        symbol.symbolLayer(0).setBrushStyle(brushStyle)
        symbol.symbolLayer(0).setStrokeColor(QColor(color))
        symbol.symbolLayer(0).setStrokeStyle(Qt.PenStyle.SolidLine)
        symbol.symbolLayer(0).setStrokeWidth(size)
        return symbol

    @staticmethod
    def createSamplingPointSymbol(geometryType, color, size, penStyle):
        symbol = QgsSymbol.defaultSymbol(geometryType)
        symbol.setColor(QColor(color))
        symbol.symbolLayer(0).setStrokeStyle(penStyle)
        symbol.symbolLayer(0).setSize(size)
        return symbol

    @staticmethod
    def createClassLabels(index, classInterval):
        if index == 0:
            label = f"> {classInterval[index + 1]}"
        elif index == 3:
            label = f"< {classInterval[index]}"
        else:
            label = f"{classInterval[index + 1]} - {classInterval[index]}"
        return label

    @staticmethod
    def calculateVectorClasses(minValue, maxValue, numberClasses):
        step = (maxValue - minValue) / numberClasses
        classes = [round((maxValue - i * step), 1) for i in range(5)]
        return classes

    @staticmethod
    def calculateClasses(minValue, maxValue, numberClasses):
        step = (maxValue - minValue) / (numberClasses - 1)
        classes = [round(minValue + i * step, 10) for i in range(numberClasses)]
        return classes

    def createRasterRenderer(self, raster):

        provider = raster.dataProvider()
        minValue, maxValue = self.getMinMaxFromRaster(provider)
        numberClasses = int(self.symbologySettings[0])

        classes = self.calculateClasses(minValue, maxValue, numberClasses)
        colors = self.symbologySettings[1]
        colorList = self.createColorRampItemList(classes, colors)

        legendSettings = self.createRasterLegendSettings()
        colorRamp = self.createRasterColorRampShader(colorList, legendSettings)
        rasterShader = self.createRasterShader(colorRamp)

        renderer = self.createRasterRendererType(provider, rasterShader)
        renderer.setClassificationMax(maxValue)
        renderer.setClassificationMin(minValue)

        return renderer

    @staticmethod
    def createColorRampItemList(classes, colors):
        colorItemList = list()
        rampItemDict = zip(classes, colors)
        for value, color in rampItemDict:
            colorItemList.append(
                QgsColorRampShader.ColorRampItem(value, QColor(color), f'{value:.1f}'))
        return colorItemList

    @staticmethod
    def getMinMaxFromRaster(rasterProvider):
        rasterStatistics = rasterProvider.bandStatistics(1, QgsRasterBandStats.All)
        return rasterStatistics.minimumValue, rasterStatistics.maximumValue

    @staticmethod
    def createRasterRendererType(rasterProvider, rasterShader):
        return QgsSingleBandPseudoColorRenderer(rasterProvider, 1, rasterShader)

    @staticmethod
    def createRasterShader(colorRamp):
        rasterShader = QgsRasterShader()
        rasterShader.setRasterShaderFunction(colorRamp)
        return rasterShader

    @staticmethod
    def createRasterLegendSettings():
        legendSettings = QgsColorRampLegendNodeSettings()
        legendSettings.setUseContinuousLegend(False)
        return legendSettings

    @staticmethod
    def createRasterColorRampShader(colorList, legendSettings):
        colorRamp = QgsColorRampShader()
        colorRamp.setColorRampItemList(colorList)
        colorRamp.setColorRampType(QgsColorRampShader.Interpolated)
        colorRamp.setLegendSettings(legendSettings)
        return colorRamp

    def applySymbology(self, layer, fieldName, raster=False):
        if raster:
            renderer = self.createRasterRenderer(layer)
        else:
            renderer = self.createSamplingLayerSymbology(layer, fieldName)
        layer.setRenderer(renderer)
        layer.triggerRepaint()

    @staticmethod
    def updateFeatures(layer, field, estimatedField, feedback):

        total = 100.0 / layer.featureCount() if layer.featureCount() else 0
        layer.startEditing()

        for index, feature in enumerate(layer.getFeatures()):
            feature[VALIDATION_FIELDS[0]] = feature[estimatedField]
            layer.updateFeature(feature)
            if bool(feature[VALIDATION_FIELDS[0]]):
                feature[VALIDATION_FIELDS[1]] = feature[field] - feature[VALIDATION_FIELDS[0]]
                feature[VALIDATION_FIELDS[2]] = math.pow(feature[VALIDATION_FIELDS[1]], 2)
                layer.updateFeature(feature)
            feedback.setProgress(int(index * total))
        layer.commitChanges()
        layer.triggerRepaint()

        return layer

    @staticmethod
    def updateRmseField(layer, estimatedField, rmse, percentualRmse, feedback):

        total = 100.0 / layer.featureCount() if layer.featureCount() else 0
        layer.startEditing()

        for index, feature in enumerate(layer.getFeatures()):
            if isinstance(feature[estimatedField], QVariant):
                pass
            else:
                feature[VALIDATION_FIELDS[3]] = rmse
                feature[VALIDATION_FIELDS[4]] = percentualRmse
                layer.updateFeature(feature)
            feedback.setProgress(int(index * total))

        layer.commitChanges()
        layer.triggerRepaint()

        return layer

    @staticmethod
    def deleteFeatures(layer):
        with edit(layer):
            for feature in layer.getFeatures():
                layer.deleteFeature(feature.id())

    @staticmethod
    def updateOutputLayer(originalLayer, modifiedLayer):
        provider = originalLayer.dataProvider()
        originalLayer.selectAll()
        originalLayer.startEditing()
        originalLayer.deleteSelectedFeatures()
        featureList = [feature for feature in modifiedLayer.getFeatures()]
        provider.addFeatures(featureList)
        originalLayer.commitChanges()
        originalLayer.triggerRepaint()
        originalLayer.invertSelection()

    @staticmethod
    def _updateOutputLayer(originalLayer, modifiedLayer):
        with edit(originalLayer):
            # Delete all features in the originalLayer
            for feature in originalLayer.getFeatures():
                originalLayer.deleteFeature(feature.id())

            # Use addFeatures with a generator expression
            provider = originalLayer.dataProvider()
            provider.addFeatures(feature for feature in modifiedLayer.getFeatures())

        # Trigger repaint outside the editing block
        originalLayer.triggerRepaint()
