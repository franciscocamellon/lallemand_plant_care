# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeostatisticsTrial
                                 A QGIS plugin
 Lallemand Plant Care
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

import os

from qgis.PyQt import QtWidgets
from qgis.PyQt.QtWidgets import QHeaderView
from qgis.core import QgsProject

from .ui_geostatistics_trial import Ui_Dialog
from ...core.constants import *
from ...core.factories.postgres_factory import PostgresFactory
from ...core.services.layer_service import LayerService
from ...core.services.message_service import MessageService
from ...core.services.system_service import SystemService
from ...core.services.widget_service import WidgetService


class GeostatisticsTrial(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        """Constructor."""
        super(GeostatisticsTrial, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Geostatistics Trial Information")
        self.project = ''
        self.layer_services = LayerService()
        self.postgresFactory = PostgresFactory()
        self.setTrialWidget()
        self.loadTrialData()
        self.fetchDomain()
        self.fetchLpcTeam()
        self.fetchCropData()
        self.fetchFarmerData()

        self.trialFieldNameLineEdit.editingFinished.connect(self.setQgisProjectName)
        self.trialAddPushButton.clicked.connect(self.register)
        self.trialEditPushButton.clicked.connect(self.updateTrialWidget)
        self.trialDeletePushButton.clicked.connect(self.deleteTrial)
        self.createQgisProjectPushButton.clicked.connect(self.saveQgisProject)

    def setTrialWidget(self):
        self.trialTableWidget.setHorizontalHeaderLabels(GEOSTATISTIC_TRIAL)
        self.trialTableWidget.verticalHeader().setVisible(True)
        self.trialTableWidget.setColumnHidden(0, True)
        self.trialTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.trialTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.trialIDLabel.hide()

        WidgetService().floatValidator(self.trialFieldAreaLineEdit)

    def updateTrialWidget(self):
        selectedData = WidgetService.getSelectedData(self.trialTableWidget, 11, 'Updating data')

        if selectedData:
            currentRow, data = selectedData
            self.geostatisticsTrialGroupBox.setTitle('Update trial')
            self.trialIDLabel.setText(data[0])
            self.trialFieldNameLineEdit.setText(data[1])
            self.trialFieldAreaLineEdit.setText(data[2])
            self.trialIrrigatedComboBox.setCurrentIndex(self.trialIrrigatedComboBox.findText(data[3]))
            self.trialSoilTypeLineEdit.setText(data[4])
            self.lpcTeamComboBox.setCurrentIndex(self.lpcTeamComboBox.findText(data[5]))
            self.farmerComboBox.setCurrentIndex(self.farmerComboBox.findText(data[6]))
            self.cropFieldComboBox.setCurrentIndex(self.cropFieldComboBox.findText(data[7]))
            self.trialAddPushButton.setText('Update')
        else:
            MessageService().messageBox('Updating data', 'No data selected.', 5, 1)

    def clearTrialWidget(self):
        self.trialIDLabel.setText('noid')
        self.trialFieldNameLineEdit.clear()
        self.trialFieldAreaLineEdit.clear()
        self.trialSoilTypeLineEdit.clear()
        self.lpcTeamComboBox.setCurrentIndex(0)
        self.farmerComboBox.setCurrentIndex(0)
        self.cropFieldComboBox.setCurrentIndex(0)

    def clearQgisProjectWidget(self):
        self.qgisProjectLineEdit.clear()
        self.trialStructureCheckBox.setChecked(False)
        self.qgisProjectFileWidget.lineEdit().clearValue()

    def register(self):
        # TODO move register to the factory
        # connection = PostgresFactory().openConnection('BD_GEOSTAT_LPC')
        buttonType = self.trialAddPushButton.text()

        if buttonType == 'Update':
            sql = UPDATE_TRIAL_SQL
            data = self.prepareTrialData()
            self.trialAddPushButton.setText('Add')
            self.geostatisticsTrialGroupBox.setTitle('Add crop')
        else:
            sql = INSERT_TRIAL_SQL
            data = self.prepareTrialData()

        result = self.postgresFactory.postSqlExecutor(sql, data)
        self.loadTrialData()
        self.clearTrialWidget()
        MessageService().resultMessage(result, 'Trial management', 'Data saved successfully!')

    def deleteTrial(self):
        selectedData = WidgetService.getSelectedData(self.trialTableWidget, 11, 'Deleting data')

        if selectedData:
            currentRow, data = selectedData
            result = self.postgresFactory.postSqlExecutor(DELETE_TRIAL_SQL.format(data[0]))
            self.loadTrialData()
            MessageService().resultMessage(result, 'Deleting data', 'Data deleted successfully!')
        else:
            MessageService().messageBox('Deleting data', 'No data selected.', 5, 1)

    def prepareTrialData(self):
        teamId = self.lpcTeamComboBox.itemData(self.lpcTeamComboBox.currentIndex())
        farmerId = self.farmerComboBox.itemData(self.farmerComboBox.currentIndex())
        cropId = self.cropFieldComboBox.itemData(self.cropFieldComboBox.currentIndex())
        irrigated = self.trialIrrigatedComboBox.itemData(self.trialIrrigatedComboBox.currentIndex())

        trialData = [
            self.trialFieldNameLineEdit.text(),
            self.trialFieldAreaLineEdit.text(),
            irrigated,
            self.trialSoilTypeLineEdit.text(),
            teamId,
            farmerId,
            cropId,
            15,
            SystemService().createDate()
        ]
        if self.trialIDLabel.text() != 'noid':
            trialData.append(self.trialIDLabel.text())

        return tuple(trialData)

    def loadTrialData(self):
        result = self.postgresFactory.getSqlExecutor(FETCH_ALL_TRIAL)

        if len(result) > 0:
            self.tableDataFormatter(result)
        else:
            WidgetService().populateTable(result, self.trialTableWidget)

    def tableDataFormatter(self, result):
        for row in result:
            lpcTeamName = self.postgresFactory.fetchOne(FETCH_ONE_TEAM, row['lpc_team'])
            farmer = self.postgresFactory.fetchOne(FETCH_ONE_FARMER, row['farmer'])
            crop = self.postgresFactory.fetchOne(FETCH_ONE_CROP, row['crop_trial'])

            row['lpc_team'] = f"{lpcTeamName[0]['first_name']} {lpcTeamName[0]['last_name']}"
            row['farmer'] = f"{farmer[0]['first_name']} {farmer[0]['last_name']}"
            row['crop_trial'] = f"{crop[0]['crop_name']} - {crop[0]['variety']}"

        WidgetService().populateTable(result, self.trialTableWidget)

    def fetchDomain(self):
        comboboxData = self.postgresFactory.fetchDataToCombobox(self.trialIrrigatedComboBox, FETCH_ALL_DOMAIN,
                                                                ['description'], 'code')
        if not comboboxData[0]:
            MessageService().messageBox('QGIS project', comboboxData[1], 5, 1)

    def fetchLpcTeam(self):
        comboboxData = self.postgresFactory.fetchDataToCombobox(self.lpcTeamComboBox, FETCH_ALL_TEAM,
                                                                ['first_name', 'last_name'], 'id')
        if not comboboxData[0]:
            MessageService().messageBox('QGIS project', comboboxData[1], 5, 1)

    def fetchCropData(self):
        comboboxData = self.postgresFactory.fetchDataToCombobox(self.cropFieldComboBox, FETCH_ALL_CROP,
                                                                ['crop_name', 'variety'], 'id', ' - ')
        if not comboboxData[0]:
            MessageService().messageBox('QGIS project', comboboxData[1], 5, 1)

    def fetchFarmerData(self):
        comboboxData = self.postgresFactory.fetchDataToCombobox(self.farmerComboBox, FETCH_ALL_FARMER,
                                                                ['first_name', 'last_name'], 'id')
        if not comboboxData[0]:
            MessageService().messageBox('QGIS project', comboboxData[1], 5, 1)

    def setQgisProjectName(self):
        self.qgisProjectLineEdit.clear()
        self.qgisProjectLineEdit.setText(self.trialFieldNameLineEdit.text())

    def saveQgisProject(self):
        try:
            self.project = QgsProject.instance()
            if os.path.exists(self.qgisProjectFileWidget.filePath()):
                self.project.setCrs(self.qgisProjectCrsWidget.crs())
                self.project.write(f'{self.qgisProjectFileWidget.filePath()}/{self.qgisProjectLineEdit.text()}.qgs')

                if self.trialStructureCheckBox.isChecked():
                    SystemService().createDirectoryStructure(self.qgisProjectFileWidget.filePath())

                MessageService().messageBox('QGIS project', 'Project saved successfully!', 3, 1)
            else:
                MessageService().messageBox('QGIS project', 'Directory does not exists!', 5, 1)

        except Exception as e:
            warningMessage = f"Error saving project: {str(e)}"
            MessageService().messageBox('QGIS project', warningMessage, 5, 1)

        finally:
            self.clearQgisProjectWidget()
