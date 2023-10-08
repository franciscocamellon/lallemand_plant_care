# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MessageService
                                 A QGIS plugin
 Lallemand - Crop Analysis Environment
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
from qgis.core import Qgis
from qgis.gui import QgsMessageBar


class MessageService:
    def __init__(self, iface):
        self.iface = iface

    def show_message(self, message, message_type="Info"):
        message_level = 0

        if message_type == "Error":
            message_level = 2
        elif message_type == "Warning":
            message_level = 1
        elif message_type == "Success":
            message_level = 3

        self.iface.messageBar().pushMessage(message_type, message, level=message_level, duration=5)
