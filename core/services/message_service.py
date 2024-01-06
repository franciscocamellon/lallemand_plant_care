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
from qgis.PyQt.QtCore import QCoreApplication, Qt
from qgis.PyQt.QtWidgets import QMessageBox, QFileDialog, QProgressDialog
from qgis.core import QgsProcessingFeedback


class MessageService:
    def __init__(self):
        pass

    @staticmethod
    def _tr(string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('MessageService', string)

    @staticmethod
    def warningMessage(title, message):
        return QMessageBox.warning(None, title, message, QMessageBox.Ok)

    @staticmethod
    def questionMessage(title, message):
        return QMessageBox.question(None, title, message, QMessageBox.Ok)

    @staticmethod
    def informationMessage(title, message):
        return QMessageBox.information(None, title, message, QMessageBox.Ok)

    @staticmethod
    def criticalMessage(title, message):
        return QMessageBox.critical(None, title, message, QMessageBox.Ok)

    @staticmethod
    def _setIconType(iconType):
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
    def _setButtonType(buttonType):
        if buttonType == 1:
            return QMessageBox.Ok
        elif buttonType == 2:
            return QMessageBox.Cancel
        elif buttonType == 3:
            return QMessageBox.Close
        elif buttonType == 4:
            return QMessageBox.Save
        elif buttonType == 5:
            return QMessageBox.Yes
        elif buttonType == 6:
            return QMessageBox.No
        elif buttonType == [1, 2]:
            return QMessageBox.Ok | QMessageBox.Cancel
        elif buttonType == [5, 6]:
            return QMessageBox.Yes | QMessageBox.No

    def resultMessage(self, result, title, message):
        if isinstance(result, bool):
            self.messageBox(title, message, 3, 1)
        else:
            self.messageBox(title, result[1], 5, 1)

    def messageBox(self, title, message, iconType, buttonType):
        messageBox = QMessageBox()
        messageBox.setWindowTitle(self._tr(title))
        messageBox.setIcon(self._setIconType(iconType))
        messageBox.setText(self._tr(message))
        messageBox.setStandardButtons(self._setButtonType(buttonType))
        messageBox.setDefaultButton(self._setButtonType(buttonType))
        choice = messageBox.exec_()
        return choice

    def standardButtonMessage(self, title, message, iconType, buttonType):
        messageBox = QMessageBox()
        messageBox.setWindowTitle(self._tr(title))
        messageBox.setIcon(self._setIconType(iconType))
        messageBox.setText(self._tr(message[0]))
        messageBox.setInformativeText(self._tr(message[1]))
        messageBox.setStandardButtons(self._setButtonType(buttonType))
        messageBox.setDefaultButton(self._setButtonType(buttonType[1]))
        choice = messageBox.exec_()
        return choice

    def saveFileDialog(self):
        fileDialog = QFileDialog()
        fileDialog.setAcceptMode(QFileDialog.AcceptSave)
        fileDialog.setNameFilter(self._tr("QGIS Project Files (*.qgz *.qgs)"))
        fileDialog.setDefaultSuffix("qgz")
        return fileDialog


class UserFeedback(QgsProcessingFeedback):

    def __init__(self, parent=None):
        super(UserFeedback, self).__init__()
        self.progressBar = QProgressDialog("Processing...", "Cancel", 0, 100, parent)
        self.progressBar.setWindowModality(Qt.WindowModal)
        self.progressBar.show()

    def setProgress(self, percent):
        self.progressBar.setValue(percent)

    # def pushInfo(self, info):
    #     self.progressBar.setLabelText(info)

    def pushConsoleInfo(self, info):
        self.progressBar.setLabelText(info)

    def pushMessage(self, message, level=0, duration=0):
        self.progressBar.setLabelText(message)

    def isCanceled(self):
        return self.progressBar.wasCanceled()

    def close(self):
        self.progressBar.close()
