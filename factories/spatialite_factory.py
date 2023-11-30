# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CropAnalysisEnvironmentDialog
                                 A QGIS plugin
 Lallemand - Crop Analysis Environment
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

from qgis.core import QgsDataSourceUri, QgsVectorLayer, QgsProject


class SpatiaLiteLayerFactory:
    @staticmethod
    def create_layer(database_path, table_name, geom_column, display_name):
        uri = QgsDataSourceUri()
        uri.setDatabase(database_path)
        schema = ''
        uri.setDataSource(schema, table_name, geom_column)

        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        QgsProject.instance().addMapLayer(vlayer)

        return vlayer
