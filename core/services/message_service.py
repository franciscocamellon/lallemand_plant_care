# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MessageService
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
from qgis.core import Qgis
from qgis.gui import QgsMessageBar
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtCore import QCoreApplication


class MessageService:
    def __init__(self):
        pass

    def show_message(self, iface, message, message_type='info'):
        message_level = 0

        if message_type == 'error':
            message_level = 2
        elif message_type == 'warning':
            message_level = 1
        elif message_type == 'success':
            message_level = 3

        iface.messageBar().pushMessage(message_type, message, level=message_level, duration=5)

    @staticmethod
    def setIconType(iconType):
        if iconType == 1:
            return QMessageBox.NoIcon
        elif iconType == 2:
            return QMessageBox.Question
        elif iconType == 3:
            return QMessageBox.Information
        elif iconType == 4:
            return QMessageBox.Warning
        else:
            return QMessageBox.Critical

    @staticmethod
    def setButtonType(buttonType):
        if buttonType == 1:
            return QMessageBox.Ok
        elif buttonType == 2:
            return QMessageBox.Cancel
        elif buttonType == 3:
            return QMessageBox.Close
        elif buttonType == 4:
            return QMessageBox.Save

    def messageBox(self, title, message, iconType, buttonType):
        messageBox = QMessageBox()
        messageBox.setWindowTitle(self.tr(title))
        messageBox.setIcon(self.setIconType(iconType))
        messageBox.setText(self.tr(message))
        messageBox.setStandardButtons(self.setButtonType(buttonType))
        messageBox.setDefaultButton(self.setButtonType(buttonType))
        messageBox.exec_()

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('MessageService', string)
