# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'validation_dlg_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 335)
        Dialog.setMinimumSize(QtCore.QSize(465, 335))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 275))
        self.tabWidget.setObjectName("tabWidget")
        self.validationTab = QtWidgets.QWidget()
        self.validationTab.setObjectName("validationTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.validationTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.validatePushButton = QtWidgets.QPushButton(self.validationTab)
        self.validatePushButton.setMinimumSize(QtCore.QSize(100, 23))
        self.validatePushButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.validatePushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.validatePushButton.setObjectName("validatePushButton")
        self.horizontalLayout_7.addWidget(self.validatePushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.parametersGroupBox = QtWidgets.QGroupBox(self.validationTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parametersGroupBox.sizePolicy().hasHeightForWidth())
        self.parametersGroupBox.setSizePolicy(sizePolicy)
        self.parametersGroupBox.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parametersGroupBox.setFont(font)
        self.parametersGroupBox.setObjectName("parametersGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.parametersGroupBox)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.validationLayerLabel = QtWidgets.QLabel(self.parametersGroupBox)
        self.validationLayerLabel.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.validationLayerLabel.setFont(font)
        self.validationLayerLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.validationLayerLabel.setObjectName("validationLayerLabel")
        self.horizontalLayout.addWidget(self.validationLayerLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.validationLayerComboBox = QgsMapLayerComboBox(self.parametersGroupBox)
        self.validationLayerComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.validationLayerComboBox.setObjectName("validationLayerComboBox")
        self.horizontalLayout_2.addWidget(self.validationLayerComboBox)
        self.fieldToEstimateComboBox = QgsFieldComboBox(self.parametersGroupBox)
        self.fieldToEstimateComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.fieldToEstimateComboBox.setObjectName("fieldToEstimateComboBox")
        self.horizontalLayout_2.addWidget(self.fieldToEstimateComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.krigingRasterLabel = QtWidgets.QLabel(self.parametersGroupBox)
        self.krigingRasterLabel.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.krigingRasterLabel.setFont(font)
        self.krigingRasterLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.krigingRasterLabel.setObjectName("krigingRasterLabel")
        self.horizontalLayout_3.addWidget(self.krigingRasterLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.krigingRasterComboBox = QgsMapLayerComboBox(self.parametersGroupBox)
        self.krigingRasterComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.krigingRasterComboBox.setObjectName("krigingRasterComboBox")
        self.horizontalLayout_4.addWidget(self.krigingRasterComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addWidget(self.parametersGroupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.validationTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.parametersGroupBox_2 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parametersGroupBox_2.sizePolicy().hasHeightForWidth())
        self.parametersGroupBox_2.setSizePolicy(sizePolicy)
        self.parametersGroupBox_2.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parametersGroupBox_2.setFont(font)
        self.parametersGroupBox_2.setObjectName("parametersGroupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.parametersGroupBox_2)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.layerLabel = QtWidgets.QLabel(self.parametersGroupBox_2)
        self.layerLabel.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.layerLabel.setFont(font)
        self.layerLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.layerLabel.setObjectName("layerLabel")
        self.horizontalLayout_5.addWidget(self.layerLabel)
        self.fieldLabel = QtWidgets.QLabel(self.parametersGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldLabel.sizePolicy().hasHeightForWidth())
        self.fieldLabel.setSizePolicy(sizePolicy)
        self.fieldLabel.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fieldLabel.setFont(font)
        self.fieldLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.fieldLabel.setObjectName("fieldLabel")
        self.horizontalLayout_5.addWidget(self.fieldLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.errorLayerComboBox = QgsMapLayerComboBox(self.parametersGroupBox_2)
        self.errorLayerComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.errorLayerComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.errorLayerComboBox.setObjectName("errorLayerComboBox")
        self.horizontalLayout_6.addWidget(self.errorLayerComboBox)
        self.errorFieldComboBox = QgsFieldComboBox(self.parametersGroupBox_2)
        self.errorFieldComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.errorFieldComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.errorFieldComboBox.setObjectName("errorFieldComboBox")
        self.horizontalLayout_6.addWidget(self.errorFieldComboBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pixelSizeXLabel = QtWidgets.QLabel(self.parametersGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelSizeXLabel.sizePolicy().hasHeightForWidth())
        self.pixelSizeXLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pixelSizeXLabel.setFont(font)
        self.pixelSizeXLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.pixelSizeXLabel.setObjectName("pixelSizeXLabel")
        self.horizontalLayout_8.addWidget(self.pixelSizeXLabel)
        self.pixelSizeYLabel = QtWidgets.QLabel(self.parametersGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelSizeYLabel.sizePolicy().hasHeightForWidth())
        self.pixelSizeYLabel.setSizePolicy(sizePolicy)
        self.pixelSizeYLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.pixelSizeYLabel.setObjectName("pixelSizeYLabel")
        self.horizontalLayout_8.addWidget(self.pixelSizeYLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pixelSizeXSpinBox = QtWidgets.QDoubleSpinBox(self.parametersGroupBox_2)
        self.pixelSizeXSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.pixelSizeXSpinBox.setDecimals(4)
        self.pixelSizeXSpinBox.setMaximum(999.99)
        self.pixelSizeXSpinBox.setSingleStep(0.1)
        self.pixelSizeXSpinBox.setProperty("value", 1.5)
        self.pixelSizeXSpinBox.setObjectName("pixelSizeXSpinBox")
        self.horizontalLayout_9.addWidget(self.pixelSizeXSpinBox)
        self.pixelSizeYSpinBox = QtWidgets.QDoubleSpinBox(self.parametersGroupBox_2)
        self.pixelSizeYSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.pixelSizeYSpinBox.setDecimals(4)
        self.pixelSizeYSpinBox.setMinimum(0.0)
        self.pixelSizeYSpinBox.setMaximum(999.99)
        self.pixelSizeYSpinBox.setSingleStep(0.1)
        self.pixelSizeYSpinBox.setProperty("value", 1.5)
        self.pixelSizeYSpinBox.setObjectName("pixelSizeYSpinBox")
        self.horizontalLayout_9.addWidget(self.pixelSizeYSpinBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.outlinePolygonCheckBox = QtWidgets.QCheckBox(self.parametersGroupBox_2)
        self.outlinePolygonCheckBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.outlinePolygonCheckBox.setObjectName("outlinePolygonCheckBox")
        self.horizontalLayout_10.addWidget(self.outlinePolygonCheckBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.boundaryLayerComboBox = QgsMapLayerComboBox(self.parametersGroupBox_2)
        self.boundaryLayerComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.boundaryLayerComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.boundaryLayerComboBox.setObjectName("boundaryLayerComboBox")
        self.horizontalLayout_11.addWidget(self.boundaryLayerComboBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.compensatePushButton = QtWidgets.QPushButton(self.parametersGroupBox_2)
        self.compensatePushButton.setMinimumSize(QtCore.QSize(100, 23))
        self.compensatePushButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.compensatePushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.compensatePushButton.setObjectName("compensatePushButton")
        self.horizontalLayout_13.addWidget(self.compensatePushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.gridLayout_3.addWidget(self.parametersGroupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.validatePushButton.setText(_translate("Dialog", "Validate"))
        self.parametersGroupBox.setTitle(_translate("Dialog", "Parameters"))
        self.validationLayerLabel.setText(_translate("Dialog", "Validation points"))
        self.krigingRasterLabel.setText(_translate("Dialog", "Ordinary kriging raster"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.validationTab), _translate("Dialog", "Validation"))
        self.parametersGroupBox_2.setTitle(_translate("Dialog", "Parameters"))
        self.layerLabel.setText(_translate("Dialog", "Error layer"))
        self.fieldLabel.setText(_translate("Dialog", "Error field"))
        self.pixelSizeXLabel.setText(_translate("Dialog", "Pixel size X"))
        self.pixelSizeYLabel.setText(_translate("Dialog", "Pixel size Y"))
        self.outlinePolygonCheckBox.setText(_translate("Dialog", "Outline polygon"))
        self.compensatePushButton.setText(_translate("Dialog", "Compensate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Error compensation"))
from qgsfieldcombobox import QgsFieldComboBox
from qgsmaplayercombobox import QgsMapLayerComboBox