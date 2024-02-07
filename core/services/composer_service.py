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
from contextlib import contextmanager

from qgis.core import (
    QgsProject,
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
    QgsLayoutExporter
)
from qgis.PyQt.QtWidgets import QMessageBox, QFileDialog
from qgis.PyQt.QtCore import Qt, QRectF
from qgis.PyQt.QtGui import QColor, QFont

from .plot_service import PlotterService
from ...gui.settings.options_settings_dlg import OptionsSettingsPage
from .message_service import MessageService
from .system_service import SystemService
from ..constants import VALIDATION_FIELDS, REFERENCE_POINTS
from ..tools.algorithm_runner import AlgorithmRunner


class ComposerService:

    def __init__(self, project):
        self.project = project

    @staticmethod
    def _setLayoutPageSize(layout, width, height):
        layoutSize = QgsLayoutSize(width, height, QgsUnitTypes.LayoutMillimeters)
        layout.pageCollection().pages()[0].setPageSize(layoutSize)

    @staticmethod
    def createItemLabel(layout, text):
        itemLabel = QgsLayoutItemLabel(layout)
        itemLabel.setText(text)
        return itemLabel.adjustSizeToText()

    @staticmethod
    def _setItemLabelFont(label, font, size, bold=False):
        if bold:
            return label.setFont(QFont(font, size, QFont.Bold))
        return label.setFont(QFont(font, size))

    @staticmethod
    def _setItemLabelColor(label, color):
        label.setFontColor(QColor(color))

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
    def _setItemMapScale(itemMap, layer):
        buffer = 1
        layer.selectAll()
        boundingBox = layer.boundingBoxOfSelected()
        extent = boundingBox.buffered(buffer)
        itemMap.setExtent(extent)
        itemMap.zoomToExtent(extent)

    @staticmethod
    def _setLegendStyle(font, size, bold=False):
        style = QgsLegendStyle()
        if bold:
            style.setFont(QFont(font, size, QFont.Bold))
        else:
            style.setFont(QFont(font, size, QFont.Normal))
        return style

    @staticmethod
    def createItemMapGrid(itemMap):
        gridStack = itemMap.grids()
        itemMapGrid = QgsLayoutItemMapGrid('Grid', itemMap)
        itemMapGrid.setIntervalX(100)
        itemMapGrid.setIntervalY(100)
        itemMapGrid.setStyle(3)
        itemMapGrid.setFrameStyle(4)
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
        itemMapGrid.setAnnotationFont(QFont("Times New Roman", 8))

        gridStack.addGrid(itemMapGrid)
        itemMap.update()

    @staticmethod
    def createLayoutExporter(layout, fileName, projectPath):
        exporter = QgsLayoutExporter(layout)
        exportedMapPath = f"{projectPath}/05_Results/03_Maps/{fileName}.png"
        exporter.exportToImage(exportedMapPath, QgsLayoutExporter.ImageExportSettings())

    def createLayout(self):
        layout = QgsPrintLayout(self.project)
        layout.initializeDefaults()
        self._setLayoutPageSize(layout, 200, 140)
        return layout

    def createTitleLabel(self, layout, title):
        label = self.createItemLabel(layout, title)
        label.setHAlign(Qt.AlignHCenter)
        label.setVAlign(Qt.AlignVCenter)
        self._setItemRectangle(label, 100, 7, 186, 8)
        self._setItemLabelFont(label, 'Times new Roman', 20, True)
        self._setItemLabelColor(label, 'black')
        self._setItemReferencePoint(label, 4)
        self._setItemPosition(label, 100, 7, 186, 8)

    def createItemMap(self, layout, layers):
        itemMap = QgsLayoutItemMap(layout)
        self._setItemRectangle(itemMap, 100, 73, 185, 120)
        itemMap.setFrameEnabled(True)
        itemMap.setFrameStrokeWidth(QgsLayoutMeasurement(0.3, QgsUnitTypes.LayoutMillimeters))
        itemMap.setBackgroundColor(QColor(255, 255, 255, 0))
        itemMap.setCrs(layers[0].crs())
        itemMap.setExtent(layers[0].extent())
        itemMap.setLayers(layers)
        itemMap.refresh()
        self._setItemReferencePoint(itemMap, 4)
        self._setItemPosition(itemMap, 100, 73, 185, 120)
        self._setItemMapScale(itemMap, layers[0])
        layout.addItem(itemMap)
        self.createItemMapGrid(itemMap)

    def createItemScaleBar(self, layout, itemMap):
        scaleBar = QgsLayoutItemScaleBar(layout)
        scaleBar.setLinkedMap(itemMap)
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
        scaleBar.setHeight(1.3)
        scaleBar.setFont(QFont("Times New Roman", 8))

        scaleBar.update()
        self._setItemReferencePoint(scaleBar, 4)
        self._setItemPosition(scaleBar, 37, 125, 50, 13)

        layout.addItem(scaleBar)

    def createItemLegend(self, layout, title, layer):
        legend = QgsLayoutItemLegend(layout)
        legend.setTitle(title)
        legend.setAutoUpdateModel(False)

        layerTree = QgsLayerTree()
        layerTreeLayer = layerTree.addLayer(layer)
        QgsLegendRenderer.setNodeLegendStyle(layerTreeLayer, QgsLegendStyle.Hidden)
        legend.model().setRootGroup(layerTree)

        legend.setStyle(QgsLegendStyle.Title, self._setLegendStyle('Times New Roman', 8, True))
        legend.setStyle(QgsLegendStyle.SymbolLabel, self._setLegendStyle('Times New Roman', 8, False))

        self._setItemReferencePoint(legend, 4)
        self._setItemPosition(legend, 170, 88, 21, 8)
        layout.addItem(legend)