# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FilterTask
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
import os

from ..constants import COMPOSER_LAYERS
from ..services.composer_service import ComposerService
from ..services.layer_service import LayerService
from ..services.message_service import UserFeedback, MessageService


class ComposerLayoutRunner:
    def __init__(self, iface, project):
        self.iface = iface
        self.feedback = UserFeedback(message='Loading...', title='Loading composer layouts')
        self.project = project
        self.filePath = self.project.homePath()
        self.exception = ''
        self.composerService = ''
        self.layerService = LayerService()
        self.messageService = MessageService(iface=self.iface)

    def run(self):
        layers = self.project.instance().mapLayers().values()
        contour = self.layerService.filterByLayerName(list(layers), ['_contour_'], inverse=True)

        filteredLayers = self.layerService.filterByLayerName(list(layers), COMPOSER_LAYERS, inverse=True)
        totalFeatures = len(filteredLayers)
        progressPerFeature = 100.0 / totalFeatures if totalFeatures else 0

        self.composerService = ComposerService(self.project)
        layerLayoutMapping = self.composerService.mapLayersToLayouts(filteredLayers)

        try:

            for layer, layoutPath in layerLayoutMapping.items():

                if os.path.isfile(layoutPath):
                    layout = self.composerService.createLayout(contour[0])
                    self.composerService.loadLayoutFromTemplate(layout, layoutPath)
                    self.composerService.updateComposerLayout(layout, layer, contour[0])

                    result = self.project.layoutManager().addLayout(layout)
                    if result:
                        self.messageService.logMessage(f'Loading layout {layout.name()}: SUCCESS', 3)

                progressIndex = list(layerLayoutMapping.keys()).index(layer)
                self.feedback.setProgress(int(progressIndex * progressPerFeature))

            self.feedback.setProgress(100)
            self.feedback.close()

            return True

        except Exception as loadException:
            self.messageService.logMessage(f'Error on loading layout template. {loadException}', 2)
            return False
