# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filtering_dlg_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 710)
        Dialog.setMinimumSize(QtCore.QSize(550, 710))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.yieldFiltering = QtWidgets.QWidget()
        self.yieldFiltering.setObjectName("yieldFiltering")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.yieldFiltering)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.yieldFiltering)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 220))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.datageLabel = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datageLabel.sizePolicy().hasHeightForWidth())
        self.datageLabel.setSizePolicy(sizePolicy)
        self.datageLabel.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.datageLabel.setFont(font)
        self.datageLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.datageLabel.setObjectName("datageLabel")
        self.horizontalLayout_20.addWidget(self.datageLabel)
        self.sortingLabel_4 = QtWidgets.QLabel(self.groupBox_4)
        self.sortingLabel_4.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sortingLabel_4.setFont(font)
        self.sortingLabel_4.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sortingLabel_4.setObjectName("sortingLabel_4")
        self.horizontalLayout_20.addWidget(self.sortingLabel_4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.harvesterDatageComboBox = QgsFieldComboBox(self.groupBox_4)
        self.harvesterDatageComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.harvesterDatageComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.harvesterDatageComboBox.setObjectName("harvesterDatageComboBox")
        self.horizontalLayout_9.addWidget(self.harvesterDatageComboBox)
        self.harvesterLayerYeldComboBox = QgsFieldComboBox(self.groupBox_4)
        self.harvesterLayerYeldComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.harvesterLayerYeldComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.harvesterLayerYeldComboBox.setObjectName("harvesterLayerYeldComboBox")
        self.horizontalLayout_9.addWidget(self.harvesterLayerYeldComboBox)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_11)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.methodLabel_2 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.methodLabel_2.sizePolicy().hasHeightForWidth())
        self.methodLabel_2.setSizePolicy(sizePolicy)
        self.methodLabel_2.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.methodLabel_2.setFont(font)
        self.methodLabel_2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.methodLabel_2.setObjectName("methodLabel_2")
        self.horizontalLayout_18.addWidget(self.methodLabel_2)
        self.sortingLabel_2 = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortingLabel_2.sizePolicy().hasHeightForWidth())
        self.sortingLabel_2.setSizePolicy(sizePolicy)
        self.sortingLabel_2.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sortingLabel_2.setFont(font)
        self.sortingLabel_2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sortingLabel_2.setObjectName("sortingLabel_2")
        self.horizontalLayout_18.addWidget(self.sortingLabel_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.treatmentLayerComboBox = QgsMapLayerComboBox(self.groupBox_4)
        self.treatmentLayerComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.treatmentLayerComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.treatmentLayerComboBox.setObjectName("treatmentLayerComboBox")
        self.horizontalLayout_6.addWidget(self.treatmentLayerComboBox)
        self.treatmentLayerIdComboBox = QgsFieldComboBox(self.groupBox_4)
        self.treatmentLayerIdComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.treatmentLayerIdComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.treatmentLayerIdComboBox.setObjectName("treatmentLayerIdComboBox")
        self.horizontalLayout_6.addWidget(self.treatmentLayerIdComboBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.methodLabel = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.methodLabel.setFont(font)
        self.methodLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.methodLabel.setObjectName("methodLabel")
        self.horizontalLayout_17.addWidget(self.methodLabel)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.boundaryLayerComboBox = QgsMapLayerComboBox(self.groupBox_4)
        self.boundaryLayerComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.boundaryLayerComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.boundaryLayerComboBox.setObjectName("boundaryLayerComboBox")
        self.horizontalLayout_8.addWidget(self.boundaryLayerComboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.gridLayout_2.addWidget(self.groupBox_4, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.yeldFilterPushButton = QtWidgets.QPushButton(self.yieldFiltering)
        self.yeldFilterPushButton.setMinimumSize(QtCore.QSize(100, 23))
        self.yeldFilterPushButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.yeldFilterPushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.yeldFilterPushButton.setObjectName("yeldFilterPushButton")
        self.horizontalLayout_13.addWidget(self.yeldFilterPushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 5, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 3, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.yieldFiltering)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.label.setObjectName("label")
        self.horizontalLayout_21.addWidget(self.label)
        self.sortingLabel_5 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortingLabel_5.sizePolicy().hasHeightForWidth())
        self.sortingLabel_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sortingLabel_5.setFont(font)
        self.sortingLabel_5.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sortingLabel_5.setObjectName("sortingLabel_5")
        self.horizontalLayout_21.addWidget(self.sortingLabel_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.targetProjection = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetProjection.sizePolicy().hasHeightForWidth())
        self.targetProjection.setSizePolicy(sizePolicy)
        self.targetProjection.setMinimumSize(QtCore.QSize(0, 23))
        self.targetProjection.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.targetProjection.setObjectName("targetProjection")
        self.horizontalLayout_5.addWidget(self.targetProjection)
        self.colonneDateComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.colonneDateComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.colonneDateComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.colonneDateComboBox.setObjectName("colonneDateComboBox")
        self.horizontalLayout_5.addWidget(self.colonneDateComboBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem6)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.sortingLabel_6 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortingLabel_6.sizePolicy().hasHeightForWidth())
        self.sortingLabel_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sortingLabel_6.setFont(font)
        self.sortingLabel_6.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sortingLabel_6.setObjectName("sortingLabel_6")
        self.horizontalLayout_22.addWidget(self.sortingLabel_6)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_22.addWidget(self.label_3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.largeurCoupeSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.largeurCoupeSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.largeurCoupeSpinBox.setDecimals(4)
        self.largeurCoupeSpinBox.setObjectName("largeurCoupeSpinBox")
        self.horizontalLayout_10.addWidget(self.largeurCoupeSpinBox)
        self.sousEchantillonnageSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.sousEchantillonnageSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sousEchantillonnageSpinBox.setDecimals(4)
        self.sousEchantillonnageSpinBox.setMinimum(1.0)
        self.sousEchantillonnageSpinBox.setObjectName("sousEchantillonnageSpinBox")
        self.horizontalLayout_10.addWidget(self.sousEchantillonnageSpinBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.addLayout(self.verticalLayout_9)
        self.gridLayout_2.addWidget(self.groupBox_2, 4, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.yieldFiltering)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 185))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.methodLabel_3 = QtWidgets.QLabel(self.groupBox_3)
        self.methodLabel_3.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.methodLabel_3.setFont(font)
        self.methodLabel_3.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.methodLabel_3.setObjectName("methodLabel_3")
        self.horizontalLayout_19.addWidget(self.methodLabel_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.harvesterLayerComboBox = QgsMapLayerComboBox(self.groupBox_3)
        self.harvesterLayerComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.harvesterLayerComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.harvesterLayerComboBox.setObjectName("harvesterLayerComboBox")
        self.horizontalLayout_4.addWidget(self.harvesterLayerComboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.crsLabel = QtWidgets.QLabel(self.groupBox_3)
        self.crsLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.crsLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.crsLabel.setObjectName("crsLabel")
        self.horizontalLayout_3.addWidget(self.crsLabel)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.crsWarningLabel = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.crsWarningLabel.setFont(font)
        self.crsWarningLabel.setStyleSheet("")
        self.crsWarningLabel.setObjectName("crsWarningLabel")
        self.horizontalLayout_3.addWidget(self.crsWarningLabel)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem10)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.reprojectCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.reprojectCheckBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.reprojectCheckBox.setObjectName("reprojectCheckBox")
        self.horizontalLayout_7.addWidget(self.reprojectCheckBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        spacerItem11 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.suggestedCrsSelectionWidget = QgsProjectionSelectionWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suggestedCrsSelectionWidget.sizePolicy().hasHeightForWidth())
        self.suggestedCrsSelectionWidget.setSizePolicy(sizePolicy)
        self.suggestedCrsSelectionWidget.setMinimumSize(QtCore.QSize(0, 23))
        self.suggestedCrsSelectionWidget.setMaximumSize(QtCore.QSize(16777215, 23))
        self.suggestedCrsSelectionWidget.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.suggestedCrsSelectionWidget.setObjectName("suggestedCrsSelectionWidget")
        self.horizontalLayout_12.addWidget(self.suggestedCrsSelectionWidget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.yieldFiltering, "")
        self.sampling = QtWidgets.QWidget()
        self.sampling.setObjectName("sampling")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.sampling)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.samplesGroupBox = QtWidgets.QGroupBox(self.sampling)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samplesGroupBox.sizePolicy().hasHeightForWidth())
        self.samplesGroupBox.setSizePolicy(sizePolicy)
        self.samplesGroupBox.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.samplesGroupBox.setFont(font)
        self.samplesGroupBox.setCheckable(True)
        self.samplesGroupBox.setChecked(False)
        self.samplesGroupBox.setObjectName("samplesGroupBox")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.samplesGroupBox)
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.totalSamplesCheckBox = QtWidgets.QCheckBox(self.samplesGroupBox)
        self.totalSamplesCheckBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.totalSamplesCheckBox.setObjectName("totalSamplesCheckBox")
        self.horizontalLayout_26.addWidget(self.totalSamplesCheckBox)
        self.eightySamplesCheckBox = QtWidgets.QCheckBox(self.samplesGroupBox)
        self.eightySamplesCheckBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.eightySamplesCheckBox.setObjectName("eightySamplesCheckBox")
        self.horizontalLayout_26.addWidget(self.eightySamplesCheckBox)
        self.twentySamplesCheckBox = QtWidgets.QCheckBox(self.samplesGroupBox)
        self.twentySamplesCheckBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.twentySamplesCheckBox.setObjectName("twentySamplesCheckBox")
        self.horizontalLayout_26.addWidget(self.twentySamplesCheckBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_26)
        self.verticalLayout_15.addLayout(self.verticalLayout_16)
        self.gridLayout_3.addWidget(self.samplesGroupBox, 2, 0, 1, 1)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem12)
        self.samplerPushButton = QtWidgets.QPushButton(self.sampling)
        self.samplerPushButton.setMinimumSize(QtCore.QSize(100, 23))
        self.samplerPushButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.samplerPushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.samplerPushButton.setObjectName("samplerPushButton")
        self.horizontalLayout_27.addWidget(self.samplerPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_27, 4, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.sampling)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.methodLabel_4 = QtWidgets.QLabel(self.groupBox_5)
        self.methodLabel_4.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.methodLabel_4.setFont(font)
        self.methodLabel_4.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.methodLabel_4.setObjectName("methodLabel_4")
        self.horizontalLayout_24.addWidget(self.methodLabel_4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.samplingLayerComboBox = QgsMapLayerComboBox(self.groupBox_5)
        self.samplingLayerComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.samplingLayerComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.samplingLayerComboBox.setObjectName("samplingLayerComboBox")
        self.horizontalLayout_14.addWidget(self.samplingLayerComboBox)
        self.verticalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem13)
        self.samplingCrsLabel = QtWidgets.QLabel(self.groupBox_5)
        self.samplingCrsLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.samplingCrsLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.samplingCrsLabel.setObjectName("samplingCrsLabel")
        self.horizontalLayout_15.addWidget(self.samplingCrsLabel)
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem14)
        self.samplingWarningLabel = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.samplingWarningLabel.setFont(font)
        self.samplingWarningLabel.setStyleSheet("")
        self.samplingWarningLabel.setObjectName("samplingWarningLabel")
        self.horizontalLayout_15.addWidget(self.samplingWarningLabel)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.verticalLayout_13.addLayout(self.horizontalLayout_15)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.gridLayout_3.addWidget(self.groupBox_5, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem16, 5, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem17, 1, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem18, 3, 0, 1, 1)
        self.tabWidget.addTab(self.sampling, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.harvesterLayerComboBox)
        Dialog.setTabOrder(self.harvesterLayerComboBox, self.treatmentLayerComboBox)
        Dialog.setTabOrder(self.treatmentLayerComboBox, self.treatmentLayerIdComboBox)
        Dialog.setTabOrder(self.treatmentLayerIdComboBox, self.boundaryLayerComboBox)
        Dialog.setTabOrder(self.boundaryLayerComboBox, self.targetProjection)
        Dialog.setTabOrder(self.targetProjection, self.largeurCoupeSpinBox)
        Dialog.setTabOrder(self.largeurCoupeSpinBox, self.sousEchantillonnageSpinBox)
        Dialog.setTabOrder(self.sousEchantillonnageSpinBox, self.yeldFilterPushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_4.setTitle(_translate("Dialog", "Treatment"))
        self.datageLabel.setText(_translate("Dialog", "Datage"))
        self.sortingLabel_4.setText(_translate("Dialog", "Rendement"))
        self.methodLabel_2.setText(_translate("Dialog", "Polygones traitement"))
        self.sortingLabel_2.setText(_translate("Dialog", "Identifiant polygones"))
        self.methodLabel.setText(_translate("Dialog", "Contour"))
        self.yeldFilterPushButton.setText(_translate("Dialog", "Filter"))
        self.groupBox_2.setTitle(_translate("Dialog", "Parameters"))
        self.label.setText(_translate("Dialog", "Target projection"))
        self.sortingLabel_5.setText(_translate("Dialog", "Colonne date"))
        self.sortingLabel_6.setText(_translate("Dialog", "Largeur coupe"))
        self.label_3.setText(_translate("Dialog", "Sous Echantillonnage"))
        self.groupBox_3.setTitle(_translate("Dialog", "Harvester points"))
        self.methodLabel_3.setText(_translate("Dialog", "Carte rendement"))
        self.crsLabel.setText(_translate("Dialog", "CRS -> "))
        self.crsWarningLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:8pt; color:#ff0000;\">**Needs to be reprojected</span></p></body></html>"))
        self.reprojectCheckBox.setText(_translate("Dialog", "Reprojection"))
        self.label_2.setText(_translate("Dialog", "Suggested CRS:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.yieldFiltering), _translate("Dialog", "Yield filtering"))
        self.samplesGroupBox.setTitle(_translate("Dialog", "Samples"))
        self.totalSamplesCheckBox.setText(_translate("Dialog", "Total"))
        self.eightySamplesCheckBox.setText(_translate("Dialog", "80% samples"))
        self.twentySamplesCheckBox.setText(_translate("Dialog", "20% samples"))
        self.samplerPushButton.setText(_translate("Dialog", "Run"))
        self.groupBox_5.setTitle(_translate("Dialog", "Filtered points"))
        self.methodLabel_4.setText(_translate("Dialog", "Layer"))
        self.samplingCrsLabel.setText(_translate("Dialog", "CRS -> "))
        self.samplingWarningLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:8pt; color:#ff0000;\">**Needs to be in UTM projection</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sampling), _translate("Dialog", "Sampling"))
from qgsfieldcombobox import QgsFieldComboBox
from qgsmaplayercombobox import QgsMapLayerComboBox
from qgsprojectionselectionwidget import QgsProjectionSelectionWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
