# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TreatmentPolygons
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

from qgis.PyQt.QtCore import QObject

from ..settings.options_settings_dlg import OptionsSettingsPage
from ...core.algorithms.algorithm_runner import AlgorithmRunner
from ...core.services.layer_service import LayerService
from ...core.services.message_service import MessageService


class TreatmentPolygons(QObject):

    def __init__(self, project):
        """Constructor."""
        super(TreatmentPolygons, self).__init__()
        self.project = project
        self.layerService = LayerService()
        self.messageService = MessageService()
        self.algRunner = AlgorithmRunner()
        self.settings = OptionsSettingsPage().getTreatmentPolygonsSettings()

    def verifyLoadedLayer(self, layerName):
        layer = self.project.mapLayersByName(layerName)
        if not layer:
            self.messageService.warningMessage('Filtering points', f'There is no {layerName} layer loaded!')
        return layer

    def runTreatmentPolygons(self):
        reproject: bool() = None
        epsg: str = ''
        print('method', self.settings[4][1])
        method = 1 if self.settings[4][1] else 0
        print('method', method)

        layer = self.verifyLoadedLayer('GPS_points')


        if layer[0].crs().isGeographic():
            crsOperations = self.layerService.getSuggestedCrs(layer[0])
            reproject = True
            epsg = crsOperations[2]

        parameters = {'GPS_POINTS_LAYER': layer[0],
                      'REPROJECT': reproject,
                      'CRS': '',
                      'SORTING_FIELD': 'ID',
                      'METHOD': method,
                      'BORDER_SIZE': float(self.settings[3]),
                      'BOUNDARY': True}



        self.algRunner.runTreatmentPolygons(epsg, parameters)