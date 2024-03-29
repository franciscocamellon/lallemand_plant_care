# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SystemService
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
import os
import datetime
import re
import shutil

from .message_service import MessageService
from ..constants import DIRECTORY_STRUCTURE


class SystemService:

    def __init__(self):
        self.messageService = MessageService()

    @staticmethod
    def filterByFileName(directoryPath, filterString):
        fileList = os.listdir(directoryPath)
        regexPattern = '|'.join(map(re.escape, filterString))
        pattern = re.compile(regexPattern)

        for file in fileList:
            if pattern.search(file):
                filePath = os.path.join(directoryPath, file)
                return os.path.normpath(filePath)

    @staticmethod
    def createDirectoryStructure(basePath):

        for mainDirectory, subDirectories in DIRECTORY_STRUCTURE.items():
            mainDirectoryPath = os.path.join(basePath, mainDirectory)

            if os.path.exists(mainDirectoryPath) and os.listdir(mainDirectoryPath):
                for subDirectory in subDirectories:
                    subDirectoryPath = os.path.join(mainDirectoryPath, subDirectory)
                    if os.path.exists(subDirectoryPath):
                        continue
                    os.makedirs(subDirectoryPath, exist_ok=True)

            os.makedirs(mainDirectoryPath, exist_ok=True)

            for subDirectory in subDirectories:
                subDirectoryPath = os.path.normpath(os.path.join(mainDirectoryPath, subDirectory))
                os.makedirs(subDirectoryPath, exist_ok=True)

    @staticmethod
    def createDate():
        createDate = datetime.datetime.now()
        return createDate.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def extractFileName(file_path):

        try:
            return os.path.splitext(os.path.basename(file_path))[0]

        except Exception as file_name_exception:
            errorMessage = f'Error getting file name: {str(file_name_exception)}'
            MessageService().messageBox('Loading file', errorMessage, 5, 1)
            return None

    @staticmethod
    def getPath(mainDirectory):

        if len(DIRECTORY_STRUCTURE[mainDirectory]) > 0:
            for subDirectory in DIRECTORY_STRUCTURE[mainDirectory]:
                return f'{mainDirectory}/{subDirectory}'
        else:
            return f'{mainDirectory}/'

    @staticmethod
    def _copyFile(source, target):
        shutil.copyfile(source, target)

    def copyVariogram(self, sourcePath, targetPath):
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)

        for resultFile in os.listdir(sourcePath):
            if "0_Variograma" in resultFile:
                oldFilePath = os.path.normpath(os.path.join(sourcePath, resultFile))
                newFilePath = os.path.normpath(os.path.join(targetPath, resultFile))
                self._copyFile(oldFilePath, newFilePath)

    def fileExist(self, path, task=False):
        if os.path.isfile(path):
            file = os.path.basename(path)
            if task:
                return True
            else:
                return self.messageService.standardButtonMessage('Load trial files',
                                                                 [f'{file} already exist!', 'Overwrite?'],
                                                                 4, [5, 6])

    def getFieldName(self, string):
        underscoreReplacedString = string.replace('_', '')
        return underscoreReplacedString[0:11]
