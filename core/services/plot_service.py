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
import matplotlib.pyplot as plt

from qgis.PyQt.QtGui import QPalette, QColor

from ...gui.settings.options_settings_dlg import OptionsSettingsPage


class PlotterService:

    def __init__(self):
        self.settings = OptionsSettingsPage().getHistogramSettings()
        self.bins = self.settings[0]
        self.color = self.settings[1].getRgbF()
        self.edgeColor = self.settings[2].getRgbF()
        self.rowLabels = ['N of samples', 'Minimum', 'Maximum', 'Sum', 'Mean', 'Standard deviation', 'Coef variation (%)']

    def createFrequencyHistogram(self, values, tableData, title, exportPng=False, path=None):
        plt.figure()
        plt.hist(values, bins=self.bins, color=self.color, edgecolor=self.edgeColor)

        stats_table = plt.table(cellText=tableData,
                                rowLabels=self.rowLabels,
                                cellLoc='center', rowLoc='center',
                                loc='lower center',
                                bbox=[0.2, -0.95, 0.9, 0.65])
        plt.subplots_adjust(left=0.15, bottom=0.45)

        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title(f'{title} Histogram')

        if exportPng:
            plt.savefig(path)
        plt.close()