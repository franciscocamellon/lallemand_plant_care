# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LoadFiles
                                 A QGIS plugin
 Lallemand Plant Care
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
import os
import processing

from qgis.PyQt import QtWidgets, uic
from qgis.core import QgsLayerTreeGroup, QgsCoordinateReferenceSystem

from .algorithm_runner import AlgorithmRunner
from ..constants import QGIS_TOC_GROUPS, POLYGONS_BUILDER_METHODS, OPERATION
from ..services.layer_service import LayerService

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), '../../gui/layer_manager/load_files.ui')
)


class LoadFiles(QtWidgets.QDialog, FORM_CLASS):

    def __init__(self, iface, project, parent=None):
        """Constructor."""
        super(LoadFiles, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface
        self.project = project
        self.layer_services = LayerService(self.iface)
        self.crsOperations = ''

        self.crsWarningLabel.hide()
        self.suggestedCrsSelectionWidget.setEnabled(False)
        self.methodComboBox.insertItems(0, POLYGONS_BUILDER_METHODS)
        self.methodComboBox.setEnabled(False)
        self.sortingFieldComboBox.setEnabled(False)
        self.reprojectCheckBox.stateChanged.connect(self.enableReprojectChildren)
        self.treatmentCheckBox.stateChanged.connect(self.enableTreatmentChildren)
        self.gpsFileWidget.fileChanged.connect(self.updateGpsUI)
        self.harvesterFileWidget.fileChanged.connect(self.updateGpsUI)
        self.loadGpsPointsPushButton.clicked.connect(self.loadGpsPoints)
        self.loadHarvesterPointsPushButton.clicked.connect(self.loadHarvesterPoints)

    def loadGpsPoints(self):
        filePath = self.gpsFileWidget.filePath()
        fileName = self.layer_services.get_file_name(self.gpsFileWidget.filePath())
        layer = self.layer_services.create_vector_layer(fileName, filePath)

        self.loadPointFile(layer, QGIS_TOC_GROUPS[0])

        epsg = self.suggestedCrsSelectionWidget.crs().authid()

        if self.reprojectCheckBox.isChecked():

            reprojected = self.reprojectLayer(layer, epsg, self.crsOperations[2])

            reprojected.setName(f'{fileName}_{self.crsOperations[0]}')

            self.loadPointFile(reprojected, QGIS_TOC_GROUPS[1])

        # if self.treatmentCheckBox.isChecked():
        #     polygons = self.createTreatmentPolygons(layer, self.methodComboBox.currentIndex(),
        #                                             self.sortingFieldComboBox.currentField())
        #     print(polygons)
        #

    def loadHarvesterPoints(self):
        filePath = self.harvesterFileWidget.filePath()
        fileName = self.layer_services.get_file_name(self.harvesterFileWidget.filePath())
        layer = self.layer_services.create_vector_layer(fileName, filePath)
        self.loadPointFile(layer)

    def loadPointFile(self, layer, groupName):

        root = self.project.instance().layerTreeRoot()
        group = root.findGroup(groupName)
        if group is not None:
            self.project.instance().addMapLayer(layer, False)
            group.addLayer(layer)
        else:
            group = QgsLayerTreeGroup(groupName)
            root.addChildNode(group)
            self.project.instance().addMapLayer(layer, False)
            group.addLayer(layer)

    @staticmethod
    def createTreatmentPolygons(layer, method, sorting):
        return AlgorithmRunner().runWaypointsPolygonsBuilder(layer, method, sorting)

    @staticmethod
    def reprojectLayer(layer, targetCrs, operation):
        return AlgorithmRunner().runReprojectLayer(layer, targetCrs, operation)

    def updateGpsUI(self, path):

        layer = self.layer_services.create_vector_layer(self.layer_services.get_file_name(path), path)
        crsInfo = self.layer_services.getSuggestedCrs(layer)
        self.crsOperations = crsInfo
        self.suggestedCrsSelectionWidget.setOptionVisible(5, False)
        self.suggestedCrsSelectionWidget.setCrs(QgsCoordinateReferenceSystem(crsInfo[1]))
        self.sortingFieldComboBox.setFields(layer.fields())

        if layer.crs().isGeographic():
            self.crsWarningLabel.show()
        self.gpsCRSLabel.setText(f'CRS -> {layer.crs().authid()}')

        del layer

    def enableReprojectChildren(self, state):
        if state == 0:
            self.suggestedCrsSelectionWidget.setEnabled(False)
        else:
            self.suggestedCrsSelectionWidget.setEnabled(True)

    def enableTreatmentChildren(self, state):
        if state == 0:
            self.methodComboBox.setEnabled(False)
            self.sortingFieldComboBox.setEnabled(False)
        else:
            self.methodComboBox.setEnabled(True)
            self.sortingFieldComboBox.setEnabled(True)
