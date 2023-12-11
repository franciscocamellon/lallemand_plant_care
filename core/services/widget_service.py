# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WidgetService
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

from qgis.PyQt import QtCore, QtWidgets
from qgis.PyQt.QtWidgets import QHeaderView

from .message_service import MessageService


class WidgetService:

    def __init__(self):
        """
        Constructor for the SystemService class.
        """
        pass

    @staticmethod
    def getSelectedData(tableWidget, totalColumns, msgTitle):
        currentRow = tableWidget.currentRow()
        selectedItems = tableWidget.selectedItems()

        if not selectedItems:
            return

        if len(selectedItems) > 0:
            data = []
            for column in range(totalColumns):
                item = tableWidget.item(currentRow, column)
                data.append(item.text())

            return currentRow, data
        else:
            MessageService().messageBox(msgTitle, 'No data selected.', 5, 1)

    @staticmethod
    def populateTable(result, tableWidget):
        tableWidget.clearContents()

        if not result:
            tableWidget.setRowCount(1)
            return

        tableWidget.setRowCount(len(result))
        keys = result[0].keys()
        tableWidget.setColumnCount(len(keys))

        for rowIdx, row in enumerate(result):
            for colIdx, key in enumerate(keys):
                value = row[key]
                if isinstance(value, datetime.datetime):
                    value = value.strftime("%d/%m/%Y") if value else ""

                item = QtWidgets.QTableWidgetItem(str(value))
                tableWidget.setItem(rowIdx, colIdx, item)