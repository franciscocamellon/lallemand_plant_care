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
from typing import Optional

from qgis.PyQt import QtWidgets
from qgis.core import QgsMapLayerProxyModel, QgsTask

from ...core.algorithms.algorithm_runner import AlgorithmRunner
from .report_dlg_base import Ui_Dialog
from ..settings.options_settings_dlg import OptionsSettingsPage
from ...core.constants import FETCH_ALL_TRIAL, FETCH_ONE_TRIAL, FETCH_ONE_FARMER, FETCH_ONE_CROP
from ...core.factories.postgres_factory import PostgresFactory
from ...core.services.layer_service import LayerService
from ...core.services.message_service import MessageService
from ...core.services.plot_service import PlotterService
from ...core.services.report_service import ReportService
from ...core.services.statistics_service import StatisticsService
from ...core.services.system_service import SystemService


class StatisticsReport(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, iface, project, parent=None):
        """Constructor."""
        super(StatisticsReport, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.project = project
        self.filePath = self.project.homePath()
        self.setWindowTitle('Statistics reports')
        self.layerService = LayerService()
        self.postgresFactory = PostgresFactory()
        self.statisticsService = StatisticsService()
        self.reportService = ReportService()
        self.systemService = SystemService()
        self.plotService = PlotterService()
        self.task: Optional[QgsTask] = None
        self.settings = OptionsSettingsPage().getKrigingSettings()
        self.layers = self.project.instance().mapLayers()
        self.setReportUI()
        self.loadTrialData()
        self.presPushButton.clicked.connect(self.runPresentation)
        self.reportPushButton.clicked.connect(self.runReport)
        # self.reportPushButton.clicked.connect(self.runReportTask)

    def setReportUI(self):
        yieldLayer = self.layerService.filterByLayerName(list(self.layers.values()),
                                                         ['filtermap', 'Yield_Map', 'T1_T2_total'])
        t1Layer = self.layerService.filterByLayerName(list(self.layers.values()), ['T1_total'])
        t2Layer = self.layerService.filterByLayerName(list(self.layers.values()), ['T2_total'])

        t1Surface = self.layerService.filterByLayerName(list(self.layers.values()), ['T1_Final_Surface_Points'])
        t2Surface = self.layerService.filterByLayerName(list(self.layers.values()), ['T2_Final_Surface_Points'])
        gainSurface = self.layerService.filterByLayerName(list(self.layers.values()), ['Gain_Points'])

        self.yieldLayerComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.t1LayerComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.t2LayerComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.gainPointsLayerComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.t1SurfacePointsComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.t2SurfacePointsComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)

        self.yieldLayerComboBox.setExceptedLayerList(yieldLayer)
        self.t1LayerComboBox.setExceptedLayerList(t1Layer)
        self.t2LayerComboBox.setExceptedLayerList(t2Layer)
        self.gainPointsLayerComboBox.setExceptedLayerList(gainSurface)
        self.t1SurfacePointsComboBox.setExceptedLayerList(t1Surface)
        self.t2SurfacePointsComboBox.setExceptedLayerList(t2Surface)

    def loadTrialData(self):
        comboboxData = self.postgresFactory.fetchDataToCombobox(self.trialComboBox, FETCH_ALL_TRIAL,
                                                                ['field_name'], 'id')
        if not comboboxData[0]:
            MessageService().messageBox('QGIS project', comboboxData[1], 5, 1)

    def getTotalPercentage(self):
        layer = self.gainPointsLayerComboBox.currentLayer()
        total, values = self.layerService.filterFeaturesByIntervals(layer)
        percentages = self.layerService.getPercentualFromIntervals(total, values, False)
        percentages.pop(0)
        return f'{sum([float(percent) for percent in percentages]):.2f}%'

    def getReportParameters(self):
        trialId = self.trialComboBox.itemData(self.trialComboBox.currentIndex())
        trialResult = self.postgresFactory.fetchOne(FETCH_ONE_TRIAL, trialId)
        farmerResult = self.postgresFactory.fetchOne(FETCH_ONE_FARMER, trialResult[0]['farmer'])
        cropResult = self.postgresFactory.fetchOne(FETCH_ONE_CROP, trialResult[0]['crop_trial'])

        yieldPoints = str(self.yieldLayerComboBox.currentLayer().featureCount())
        t1Points = str(self.t1LayerComboBox.currentLayer().featureCount())
        t2Points = str(self.t2LayerComboBox.currentLayer().featureCount())

        t1SurfaceLayer = self.t1SurfacePointsComboBox.currentLayer()
        t2SurfaceLayer = self.t2SurfacePointsComboBox.currentLayer()

        fValue, pValue = self.statisticsService.calculateAnovaTest('yield', t1SurfaceLayer, t2SurfaceLayer)
        t1Mean = self.statisticsService.calculateMean(t1SurfaceLayer, 'yield')
        t2Mean = self.statisticsService.calculateMean(t2SurfaceLayer, 'yield')
        meanDifference = t1Mean - t2Mean
        t1StdDev = self.statisticsService.calculateStdDev(t1SurfaceLayer, 'yield')
        t2StdDev = self.statisticsService.calculateStdDev(t2SurfaceLayer, 'yield')

        mapsPath = f"{self.filePath}/05_Results/03_Maps/"
        rootPath = f"{self.filePath}/05_Results/"

        reportData = {

            '{FIELD_NAME}': trialResult[0]['field_name'],
            '{field_area}': trialResult[0]['field_area'],
            '{crop_name}': cropResult[0]['crop_name'],
            '{variety}': cropResult[0]['variety'],
            '{sowing_date}': cropResult[0]['sowing_date'],
            '{harvest_date}': cropResult[0]['harvest_date'],
            '{inter_ro_cm}': str(cropResult[0]['inter_ro_cm']),
            '{field_soil}': trialResult[0]['field_soil'],
            '{field_irrigation}': str(trialResult[0]['field_irrigation']),
            '{first_name}': farmerResult[0]['first_name'],
            '{last_name}': farmerResult[0]['last_name'],
            '{town}': farmerResult[0]['town'],
            '{zipcode}': farmerResult[0]['zipcode'],
            '{TOTAL_YIELD_POINTS}': yieldPoints,
            '{TOTAL_T1_POINTS}': t1Points,
            '{TOTAL_T2_POINTS}': t2Points,
            '{TOTAL_PERCENTAGE}': self.getTotalPercentage(),
            '{MEAN_DIFFERENCE}': f'{meanDifference:.4f}'
        }
        tableData = {
            '{P_VALUE}': f'{pValue:.4f}',
            '{T1_MEAN}': f'{t1Mean:.4f}',
            '{T2_MEAN}': f'{t2Mean:.4f}',
            '{T1_STD_DEV}': f'{t1StdDev:.4f}',
            '{T2_STD_DEV}': f'{t2StdDev:.4f}'
        }

        imageData = {
            '{T1_T2_POINTS}': [self.systemService.filterByFileName(mapsPath, ['01_Points_with_measured_yield_values']),
                               4.32],
            '{T1_POINTS}': [self.systemService.filterByFileName(mapsPath, ['02_T1_Measured_yield']), 3.13],
            '{T2_POINTS}': [self.systemService.filterByFileName(mapsPath, ['03_T2_Measured_yield']), 3.13],
            '{T1_T2_MODEL}': [self.systemService.filterByFileName(mapsPath, ['06_Model_T1_T2']), 4.32],
            '{T1_MODEL}': [self.systemService.filterByFileName(mapsPath, ['07_Model_T1']), 3.13],
            '{T2_MODEL}': [self.systemService.filterByFileName(mapsPath, ['08_Model_T2']), 3.13],
            '{YIELD_GAIN_HISTOGRAM}': [self.systemService.filterByFileName(rootPath, ['Yield_Gain_Histogram']), 5.1]
        }

        return reportData, tableData, imageData

    def runReportTask(self):
        self.statisticsService.runStatistics(self.gainPointsLayerComboBox.currentLayer())

    def runReport(self):
        # 'TRIAL_NAME':,
        # 'YIELD':,
        # 'T1_LAYER':,
        # 'T2_LAYER':,
        # 'T1_SURFACE':,
        # 'T2_SURFACE':,
        # 'GAIN_POINTS':,
        # 'OUTPUT':
        # self.feedback = UserFeedback(message='Creating report...', title='Trial Report')
        # reportData, tableData, imageData = self.getReportParameters()
        # self.reportService.createWordReport(reportData, tableData, imageData, self.filePath,
        #                                     self.feedback)
        # self.close()
        # self.feedback.close()

        yieldLayer = self.layerService.filterVectorLayerByName(list(self.layers.values()), ['Yield_Map'], inverse=True)
        t1Layer = self.layerService.filterVectorLayerByName(list(self.layers.values()), ['T1_total'], inverse=True)
        t2Layer = self.layerService.filterVectorLayerByName(list(self.layers.values()), ['T2_total'], inverse=True)

        t1Surface = self.layerService.filterVectorLayerByName(list(self.layers.values()), ['T1_Final_Surface_Points'], inverse=True)
        t2Surface = self.layerService.filterVectorLayerByName(list(self.layers.values()), ['T2_Final_Surface_Points'], inverse=True)
        gainPoints = self.layerService.filterVectorLayerByName(list(self.layers.values()), ['Gain_Points'], inverse=True)

        parameters = {
            'TRIAL_NAME': '',
            'YIELD': yieldLayer,
            'T1_LAYER': t1Layer,
            'T2_LAYER': t2Layer,
            'T1_SURFACE': t1Surface,
            'T2_SURFACE': t2Surface,
            'GAIN_POINTS': gainPoints,
            'OUTPUT': ''
        }
        AlgorithmRunner().runCreateReport(parameters, self.project)

    def getPresentationParameters(self):
        trialId = self.trialComboBox.itemData(self.trialComboBox.currentIndex())
        trialResult = self.postgresFactory.fetchOne(FETCH_ONE_TRIAL, trialId)

        histogramPath = f"{self.filePath}/05_Results/01_Histograms/"
        variogramPath = f"{self.filePath}/05_Results/02_Variograms/"
        mapsPath = f"{self.filePath}/05_Results/03_Maps/"
        rootPath = f"{self.filePath}/05_Results/"

        presentationData = {
            1: {1: trialResult[0]['field_name']},
            2: {
                10: self.systemService.filterByFileName(mapsPath, ['01_Points_with_measured_yield_values']),
                11: self.systemService.filterByFileName(mapsPath, ['02_T1_Measured_yield']),
                12: self.systemService.filterByFileName(mapsPath, ['03_T2_Measured_yield'])},
            3: {
                10: self.systemService.filterByFileName(histogramPath, ['Yield_Map_V']),
                11: self.systemService.filterByFileName(histogramPath, ['T1_total_V']),
                12: self.systemService.filterByFileName(histogramPath, ['T2_total_V'])},

            5: {
                10: self.systemService.filterByFileName(mapsPath, ['06_Model_T1_T2']),
                11: self.systemService.filterByFileName(mapsPath, ['07_Model_T1']),
                12: self.systemService.filterByFileName(mapsPath, ['08_Model_T2']),
                13: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T1_T2_total_']),
                14: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T1_total_']),
                15: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T2_total_'])},
            6: {
                10: self.systemService.filterByFileName(mapsPath, ['04_T1_Sample_for_model_generation']),
                11: self.systemService.filterByFileName(mapsPath, ['07_Model_T1']),
                12: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T1_80_perc_']),
                13: self.systemService.filterByFileName(histogramPath, ['T1_80_perc_H'])},
            7: {
                10: self.systemService.filterByFileName(mapsPath, ['05_T2_Sample_for_model_generation']),
                11: self.systemService.filterByFileName(mapsPath, ['08_Model_T2']),
                12: self.systemService.filterByFileName(variogramPath, ['0_Variograma_T2_80_perc_']),
                13: self.systemService.filterByFileName(histogramPath, ['T2_80_perc_H'])},
            8: {
                10: self.systemService.filterByFileName(mapsPath, ['11_Yield_gain_using_T2']),
                11: self.systemService.filterByFileName(rootPath, ['Yield_Gain_Histogram']),
                12: self.systemService.filterByFileName(rootPath, ['Gain_Statistics_Table'])}
        }

        return presentationData

    def runPresentation(self):
        # maximum = 5
        # progress = UserFeedback(message='Creating report...', title='Statistics report')
        # # progress = QProgressDialog('Gerando apresentação.' + '...', 'Cancelar', 1, maximum, self)
        # progress.show()
        # time.sleep(0.1)
        # self.close()
        # rootPath = f"{self.filePath}/05_Results/"
        # progress.setProgress(1)
        # pValue, anovaStats = self.getAnovaStatistics()
        # progress.setProgress(2)
        # gainStats = self.getGainStatistics()
        # progress.setProgress(3)
        # self.plotService.createGainStatisticsTable(pValue, gainStats, anovaStats, True, rootPath)
        # progress.setProgress(4)
        # self.reportService.createPresentation(self.getPresentationParameters(), self.filePath)
        # progress.setProgress(5)
        self.reportService.iterate_over_slides()

    def getGainStatistics(self):
        gainStatsList = list()
        gainStats = self.statisticsService.getGainStatistics(self.gainPointsLayerComboBox.currentLayer(), 'yield')
        for statistic in gainStats:
            gainStatsList.append([f'{statistic:.2f}'])
        return gainStatsList

    def getAnovaStatistics(self):
        anovaStatsList = list()
        t1SurfaceLayer = self.t1SurfacePointsComboBox.currentLayer()
        t2SurfaceLayer = self.t2SurfacePointsComboBox.currentLayer()
        fValue, pValue = self.statisticsService.calculateAnovaTest('yield', t1SurfaceLayer, t2SurfaceLayer)
        anovaStats = self.statisticsService.getAnovaStatistics('yield', t1SurfaceLayer, t2SurfaceLayer)

        for statisticList in anovaStats:
            formattedStatisticList = [f'{statistic:.2f}' for statistic in statisticList]
            anovaStatsList.append(formattedStatisticList)

        return f'{pValue:.2f}', anovaStatsList
