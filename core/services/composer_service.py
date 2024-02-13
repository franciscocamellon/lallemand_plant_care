# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ComposerService
                                 A QGIS plugin
 Lallemand Plant Care
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-01-28
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
from collections import OrderedDict
from contextlib import contextmanager

from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsRasterLayer,
    QgsLayerTree,
    QgsPrintLayout,
    QgsLayoutPoint,
    QgsLayoutItem,
    QgsLayoutItemLabel,
    QgsLayoutItemMap,
    QgsLayoutItemMapGrid,
    QgsLayoutItemScaleBar,
    QgsLayoutItemLegend,
    QgsLegendRenderer,
    QgsLegendStyle,
    QgsUnitTypes,
    QgsLayoutSize,
    QgsLayoutMeasurement,
    QgsLayoutExporter,
    QgsTextFormat, QgsFontUtils, QgsMapLayerLegendUtils, QgsReadWriteContext
)
from qgis.PyQt.QtXml import QDomDocument
from qgis.PyQt.QtWidgets import QMessageBox, QFileDialog
from qgis.PyQt.QtCore import Qt, QRectF
from qgis.PyQt.QtGui import QColor, QFont

from .layer_service import LayerService
from .plot_service import PlotterService
from ...gui.settings.options_settings_dlg import OptionsSettingsPage
from .message_service import MessageService
from .system_service import SystemService
from ..constants import VALIDATION_FIELDS, REFERENCE_POINTS, COMPOSER_LAYOUTS, QGIS_TOC_GROUPS
from ..tools.algorithm_runner import AlgorithmRunner


class ComposerService:

    def __init__(self, project):
        self.project = project
        self.extent = ''
        self.crs = ''
        self.fontName = 'Times new Roman'
        self.filePath = self.project.homePath()
        self.layerService = LayerService()
        self._hideGroupsOnLegend(project)

    @staticmethod
    def _setLayoutPageSize(layout, width, height):
        layoutSize = QgsLayoutSize(width, height, QgsUnitTypes.LayoutMillimeters)
        layout.pageCollection().pages()[0].setPageSize(layoutSize)

    @staticmethod
    def _setItemLabelFont(item, font, size, style=None):

        if style == 'bold':
            font = QFont(font, size, QFont.Bold)
        elif style == 'light':
            font = QFont(font, size, QFont.Light)
        else:
            font = QFont(font, size, QFont.Normal)

        return item.setFont(font)

    @staticmethod
    def _setItemRectangle(item, x, y, width, height):
        item.setRect(QRectF(x, y, width, height))

    @staticmethod
    def _setItemReferencePoint(item, referencePoint):
        if referencePoint in REFERENCE_POINTS:
            item.setReferencePoint(REFERENCE_POINTS[referencePoint])

    @staticmethod
    def _setItemPosition(item, x, y, width, height):
        item.attemptMove(
            QgsLayoutPoint(x, y, QgsUnitTypes.LayoutMillimeters))
        item.attemptResize(
            QgsLayoutSize(width, height, QgsUnitTypes.LayoutMillimeters))

    @staticmethod
    def _setLegendStyle(font, size, bold=False):
        style = QgsLegendStyle()
        if bold:
            style.setFont(QFont(font, size, QFont.Bold))
        else:
            style.setFont(QFont(font, size, QFont.Normal))
        return style

    @staticmethod
    def createItemMapGrid(itemMap, fontName):
        gridStack = itemMap.grids()
        itemMapGrid = QgsLayoutItemMapGrid('Grid', itemMap)
        itemMapGrid.setIntervalX(100)
        itemMapGrid.setIntervalY(100)
        itemMapGrid.setStyle(3)

        itemMapGrid.setFrameStyle(3)
        itemMapGrid.setFrameDivisions(1, 0)
        itemMapGrid.setFrameDivisions(2, 2)
        itemMapGrid.setFrameDivisions(3, 1)
        itemMapGrid.setFrameDivisions(3, 3)
        itemMapGrid.setFrameWidth(1.0)
        itemMapGrid.setFramePenSize(0.3)

        itemMapGrid.setAnnotationEnabled(True)
        itemMapGrid.setAnnotationFrameDistance(1.5)
        itemMapGrid.setAnnotationDisplay(1, 0)
        itemMapGrid.setAnnotationDisplay(2, 2)
        itemMapGrid.setAnnotationDisplay(3, 1)
        itemMapGrid.setAnnotationDisplay(3, 3)
        itemMapGrid.setAnnotationDirection(2, 0)
        itemMapGrid.setAnnotationDirection(1, 0)
        itemMapGrid.setAnnotationPrecision(0)
        itemMapGrid.setAnnotationFont(QFont(fontName, 8))

        gridStack.addGrid(itemMapGrid)

    @staticmethod
    def _setItemScaleBarStyle(scaleBar):
        scaleBar.setStyle('Line Ticks Up')
        scaleBar.setUnits(QgsUnitTypes.DistanceMeters)
        scaleBar.setSegmentSizeMode(0)
        scaleBar.setNumberOfSegmentsLeft(0)
        scaleBar.setNumberOfSegments(4)
        scaleBar.setUnitsPerSegment(25)
        scaleBar.setMinimumBarWidth(10)
        scaleBar.setMaximumBarWidth(40)
        scaleBar.setLabelBarSpace(0.7)
        scaleBar.setLineWidth(0.3)
        scaleBar.setUnitLabel('m')
        scaleBar.setHeight(1.0)

    @staticmethod
    def _hideGroupsOnLegend(project):
        root = project.instance().layerTreeRoot()

        for group in QGIS_TOC_GROUPS:
            groupTreeLayer = root.findGroup(group)
            QgsLegendRenderer.setNodeLegendStyle(groupTreeLayer, QgsLegendStyle.Hidden)

    @staticmethod
    def _hideLayersOnLegend(legendModel, layers):
        for layer in layers:
            layerTreeLayer = legendModel.rootGroup().findLayer(layer)
            QgsLegendRenderer.setNodeLegendStyle(layerTreeLayer, QgsLegendStyle.Hidden)

    @staticmethod
    def loadLayoutFromTemplate(layout, layoutPath):
        template = QDomDocument()
        template.setContent(open(layoutPath).read())
        layout.loadFromTemplate(template, QgsReadWriteContext())

    def _setItemMapScale(self, itemMap):
        buffer = 75
        extent = self.extent.extent().buffered(buffer)
        itemMap.setExtent(extent)
        itemMap.zoomToExtent(extent)

    def createLayout(self, extent):
        self.extent = extent
        self.crs = self.extent.crs()
        layout = QgsPrintLayout(self.project)
        layout.initializeDefaults()
        self._setLayoutPageSize(layout, 200, 140)
        return layout

    def updateTitleLabel(self, label):

        label.setHAlign(Qt.AlignHCenter)
        label.setVAlign(Qt.AlignVCenter)
        self._setItemRectangle(label, 100, 7, 186, 10)
        self._setItemLabelFont(label, self.fontName, 20, 'bold')
        label.setFontColor(QColor('black'))
        self._setItemReferencePoint(label, 4)
        self._setItemPosition(label, 100, 7, 186, 10)

        label.refresh()

    def updateCrsLabelGroup(self, layout, layer):
        crsLabel = layout.itemById('crs_description')
        crsLabel.setText(layer.crs().description())
        self._setItemLabelFont(crsLabel, self.fontName, 8)
        self._setItemPosition(crsLabel, 170, 127.5, 45, 4)
        crsLabel.refresh()

        crsTitle = layout.itemById('crs_title')
        self._setItemLabelFont(crsTitle, self.fontName, 8)
        self._setItemPosition(crsTitle, 170, 124, 45, 4)
        crsTitle.refresh()

        dataOwner = layout.itemById('data_owner')
        self._setItemLabelFont(dataOwner, self.fontName, 8)
        self._setItemPosition(dataOwner, 170, 131, 45, 4)
        dataOwner.refresh()

    def updateItemMap(self, itemMap, layer, contour):

        self._setItemRectangle(itemMap, 100, 73, 185, 120)

        itemMap.setFrameEnabled(True)
        itemMap.setFrameStrokeWidth(QgsLayoutMeasurement(0.3, QgsUnitTypes.LayoutMillimeters))
        itemMap.setBackgroundColor(QColor(255, 255, 255, 0))
        itemMap.setCrs(self.crs)

        self._setItemMapScale(itemMap)

        itemMap.setLayers([contour, layer])
        itemMap.refresh()

        self._setItemReferencePoint(itemMap, 4)
        self._setItemPosition(itemMap, 100, 73, 185, 120)
        self.createItemMapGrid(itemMap, self.fontName)

        itemMap.update()

    def updateItemScaleBar(self, scaleBar, itemMap):
        scaleBar.setLinkedMap(itemMap)
        self._setItemScaleBarStyle(scaleBar)
        self._setItemLabelFont(scaleBar, self.fontName, 8, 'light')
        scaleBar.update()
        self._setItemReferencePoint(scaleBar, 3)
        self._setItemPosition(scaleBar, 10, 127, 40, 7.5)

        scaleBar.refresh()

    def updateItemLegend(self, legend, itemMap, title, layer, contour):

        legend.setLinkedMap(itemMap)
        legend.setTitle(title)
        legend.setAutoUpdateModel(True)
        legend.setBackgroundEnabled(False)
        legend.setLegendFilterByMapEnabled(True)
        legend.updateFilterByMap(True)
        legend.setAutoUpdateModel(False)

        self._hideLayersOnLegend(legend.model(), [layer, contour])

        legend.setStyle(QgsLegendStyle.Title, self._setLegendStyle(self.fontName, 10, True))
        legend.setStyle(QgsLegendStyle.SymbolLabel, self._setLegendStyle(self.fontName, 8, False))

        self._setItemReferencePoint(legend, 4)
        self._setItemPosition(legend, 170, 97, 20, 26)

        legend.updateLegend()
        legend.refresh()

    def mapLayersToLayouts(self, layers):
        layerLayoutMapping = OrderedDict()
        layouts = self.layerService.listQptFiles()
        for layer in layers:
            matchedLayoutPath = None
            for part, partialFilename in COMPOSER_LAYOUTS.items():
                if re.match(part, layer.name(), re.IGNORECASE):
                    for filePath in layouts:
                        if partialFilename in os.path.basename(filePath):
                            matchedLayoutPath = filePath
                            break
            if matchedLayoutPath:
                layerLayoutMapping[layer] = matchedLayoutPath

        return layerLayoutMapping

    def updateComposerLayout(self, layout, layer, contour):
        itemLabelTitle = layout.itemById('title')
        self.updateTitleLabel(itemLabelTitle)

        itemMap = layout.itemById('map')
        self.updateItemMap(itemMap, layer, contour)

        itemScaleBar = layout.itemById('scalebar')
        self.updateItemScaleBar(itemScaleBar, itemMap)

        itemLegend = layout.itemById('legend')
        self.updateItemLegend(itemLegend, itemMap, 'Yield (kg)', layer, contour)

        self.updateCrsLabelGroup(layout, layer)

    @staticmethod
    def overrideExportSettings(layout):
        exportSettings = QgsLayoutExporter.ImageExportSettings()
        exportSettings.flags = layout.renderContext().flags()
        exportSettings.dpi = 300
        if layout.customProperty('exportWorldFile') in ['true', True]:
            exportSettings.generateWorldFile = True

        if layout.customProperty('imageCropToContents') in ['true', True]:
            exportSettings.cropToContents = True

        return exportSettings

    def createLayoutExporter(self, layout, fileName):
        exportSettings = self.overrideExportSettings(layout)
        exporter = QgsLayoutExporter(layout)
        exporter.layout().refresh()
        exportedMapPath = f"{self.filePath}/05_Results/03_Maps/{fileName}.png"
        result = exporter.exportToImage(exportedMapPath, exportSettings)

        return result == QgsLayoutExporter.Success
