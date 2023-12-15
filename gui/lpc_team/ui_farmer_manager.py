# -*- coding: utf-8 -*-

# OptionsSettingsForm implementation generated from reading ui file 'farmer_manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FarmerDialog(object):
    def setupUi(self, FarmerDialog):
        FarmerDialog.setObjectName("FarmerDialog")
        FarmerDialog.resize(715, 590)
        FarmerDialog.setMinimumSize(QtCore.QSize(715, 590))
        FarmerDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(FarmerDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.farmerTabWidget = QtWidgets.QTabWidget(FarmerDialog)
        self.farmerTabWidget.setObjectName("farmerTabWidget")
        self.farmerTab = QtWidgets.QWidget()
        self.farmerTab.setObjectName("farmerTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.farmerTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.farmersGroupBox = QtWidgets.QGroupBox(self.farmerTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.farmersGroupBox.sizePolicy().hasHeightForWidth())
        self.farmersGroupBox.setSizePolicy(sizePolicy)
        self.farmersGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.farmersGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.farmersGroupBox.setFont(font)
        self.farmersGroupBox.setObjectName("farmersGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.farmersGroupBox)
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.farmerTableWidget = QtWidgets.QTableWidget(self.farmersGroupBox)
        self.farmerTableWidget.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerTableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.farmerTableWidget.setAlternatingRowColors(True)
        self.farmerTableWidget.setObjectName("farmerTableWidget")
        self.farmerTableWidget.setColumnCount(9)
        self.farmerTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.farmerTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmerTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmerTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmerTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmerTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmerTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmerTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmerTableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.farmerTableWidget.setHorizontalHeaderItem(8, item)
        self.horizontalLayout_3.addWidget(self.farmerTableWidget)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.farmersGroupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.farmerGroupBox = QtWidgets.QGroupBox(self.farmerTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.farmerGroupBox.sizePolicy().hasHeightForWidth())
        self.farmerGroupBox.setSizePolicy(sizePolicy)
        self.farmerGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.farmerGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.farmerGroupBox.setFont(font)
        self.farmerGroupBox.setObjectName("farmerGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.farmerGroupBox)
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.farmerAddressLabel = QtWidgets.QLabel(self.farmerGroupBox)
        self.farmerAddressLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerAddressLabel.setObjectName("farmerAddressLabel")
        self.horizontalLayout_4.addWidget(self.farmerAddressLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.farmerAddressLineEdit = QtWidgets.QLineEdit(self.farmerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.farmerAddressLineEdit.sizePolicy().hasHeightForWidth())
        self.farmerAddressLineEdit.setSizePolicy(sizePolicy)
        self.farmerAddressLineEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.farmerAddressLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerAddressLineEdit.setObjectName("farmerAddressLineEdit")
        self.horizontalLayout_10.addWidget(self.farmerAddressLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.farmerTownLabel = QtWidgets.QLabel(self.farmerGroupBox)
        self.farmerTownLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerTownLabel.setObjectName("farmerTownLabel")
        self.horizontalLayout_15.addWidget(self.farmerTownLabel)
        self.farmerCountryLabel = QtWidgets.QLabel(self.farmerGroupBox)
        self.farmerCountryLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerCountryLabel.setObjectName("farmerCountryLabel")
        self.horizontalLayout_15.addWidget(self.farmerCountryLabel)
        self.farmerZipcodeLabel = QtWidgets.QLabel(self.farmerGroupBox)
        self.farmerZipcodeLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerZipcodeLabel.setObjectName("farmerZipcodeLabel")
        self.horizontalLayout_15.addWidget(self.farmerZipcodeLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.farmerTown = QtWidgets.QLineEdit(self.farmerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.farmerTown.sizePolicy().hasHeightForWidth())
        self.farmerTown.setSizePolicy(sizePolicy)
        self.farmerTown.setMinimumSize(QtCore.QSize(0, 23))
        self.farmerTown.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerTown.setObjectName("farmerTown")
        self.horizontalLayout_16.addWidget(self.farmerTown)
        self.farmerCountry = QtWidgets.QLineEdit(self.farmerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.farmerCountry.sizePolicy().hasHeightForWidth())
        self.farmerCountry.setSizePolicy(sizePolicy)
        self.farmerCountry.setMinimumSize(QtCore.QSize(0, 23))
        self.farmerCountry.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerCountry.setObjectName("farmerCountry")
        self.horizontalLayout_16.addWidget(self.farmerCountry)
        self.farmerZipCode = QtWidgets.QLineEdit(self.farmerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.farmerZipCode.sizePolicy().hasHeightForWidth())
        self.farmerZipCode.setSizePolicy(sizePolicy)
        self.farmerZipCode.setMinimumSize(QtCore.QSize(0, 23))
        self.farmerZipCode.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerZipCode.setObjectName("farmerZipCode")
        self.horizontalLayout_16.addWidget(self.farmerZipCode)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.gridLayout_7.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.farmerFirstNameLabel = QtWidgets.QLabel(self.farmerGroupBox)
        self.farmerFirstNameLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerFirstNameLabel.setObjectName("farmerFirstNameLabel")
        self.horizontalLayout_5.addWidget(self.farmerFirstNameLabel)
        self.farmerLastNameLabel = QtWidgets.QLabel(self.farmerGroupBox)
        self.farmerLastNameLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerLastNameLabel.setObjectName("farmerLastNameLabel")
        self.horizontalLayout_5.addWidget(self.farmerLastNameLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.farmerFirstNameLineEdit = QtWidgets.QLineEdit(self.farmerGroupBox)
        self.farmerFirstNameLineEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.farmerFirstNameLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerFirstNameLineEdit.setObjectName("farmerFirstNameLineEdit")
        self.horizontalLayout_6.addWidget(self.farmerFirstNameLineEdit)
        self.farmerLastNameLineEdit = QtWidgets.QLineEdit(self.farmerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.farmerLastNameLineEdit.sizePolicy().hasHeightForWidth())
        self.farmerLastNameLineEdit.setSizePolicy(sizePolicy)
        self.farmerLastNameLineEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.farmerLastNameLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerLastNameLineEdit.setObjectName("farmerLastNameLineEdit")
        self.horizontalLayout_6.addWidget(self.farmerLastNameLineEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.gridLayout_7.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.farmerIDLabel = QtWidgets.QLabel(self.farmerGroupBox)
        self.farmerIDLabel.setEnabled(True)
        self.farmerIDLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.farmerIDLabel.setObjectName("farmerIDLabel")
        self.horizontalLayout_9.addWidget(self.farmerIDLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.farmerAddPushButton = QtWidgets.QPushButton(self.farmerGroupBox)
        self.farmerAddPushButton.setMinimumSize(QtCore.QSize(110, 30))
        self.farmerAddPushButton.setMaximumSize(QtCore.QSize(110, 16777215))
        self.farmerAddPushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":plugins/lallemand_plant_care/icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.farmerAddPushButton.setIcon(icon)
        self.farmerAddPushButton.setObjectName("farmerAddPushButton")
        self.horizontalLayout_9.addWidget(self.farmerAddPushButton)
        self.gridLayout_7.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.farmerGroupBox)
        self.farmerManagerGroupBox = QtWidgets.QGroupBox(self.farmerTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.farmerManagerGroupBox.sizePolicy().hasHeightForWidth())
        self.farmerManagerGroupBox.setSizePolicy(sizePolicy)
        self.farmerManagerGroupBox.setMinimumSize(QtCore.QSize(0, 85))
        self.farmerManagerGroupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.farmerManagerGroupBox.setFont(font)
        self.farmerManagerGroupBox.setObjectName("farmerManagerGroupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.farmerManagerGroupBox)
        self.gridLayout_8.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.farmerEditPushButton = QtWidgets.QPushButton(self.farmerManagerGroupBox)
        self.farmerEditPushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.farmerEditPushButton.setMaximumSize(QtCore.QSize(110, 30))
        self.farmerEditPushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":plugins/lallemand_plant_care/icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.farmerEditPushButton.setIcon(icon1)
        self.farmerEditPushButton.setIconSize(QtCore.QSize(24, 24))
        self.farmerEditPushButton.setObjectName("farmerEditPushButton")
        self.horizontalLayout_17.addWidget(self.farmerEditPushButton)
        self.farmerDeletePushButton = QtWidgets.QPushButton(self.farmerManagerGroupBox)
        self.farmerDeletePushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.farmerDeletePushButton.setMaximumSize(QtCore.QSize(110, 30))
        self.farmerDeletePushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":plugins/lallemand_plant_care/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.farmerDeletePushButton.setIcon(icon2)
        self.farmerDeletePushButton.setIconSize(QtCore.QSize(24, 24))
        self.farmerDeletePushButton.setObjectName("farmerDeletePushButton")
        self.horizontalLayout_17.addWidget(self.farmerDeletePushButton)
        self.gridLayout_8.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.farmerManagerGroupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.farmerTabWidget.addTab(self.farmerTab, "")
        self.cropTab = QtWidgets.QWidget()
        self.cropTab.setObjectName("cropTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.cropTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cropGroupBox = QtWidgets.QGroupBox(self.cropTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropGroupBox.sizePolicy().hasHeightForWidth())
        self.cropGroupBox.setSizePolicy(sizePolicy)
        self.cropGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.cropGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cropGroupBox.setFont(font)
        self.cropGroupBox.setObjectName("cropGroupBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.cropGroupBox)
        self.gridLayout_11.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_11.setSpacing(5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.cropTableWidget = QtWidgets.QTableWidget(self.cropGroupBox)
        self.cropTableWidget.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropTableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cropTableWidget.setAlternatingRowColors(True)
        self.cropTableWidget.setObjectName("cropTableWidget")
        self.cropTableWidget.setColumnCount(8)
        self.cropTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cropTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cropTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cropTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.cropTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.cropTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.cropTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.cropTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.cropTableWidget.setHorizontalHeaderItem(7, item)
        self.horizontalLayout_13.addWidget(self.cropTableWidget)
        self.gridLayout_11.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.cropGroupBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.registerCropGroupBox = QtWidgets.QGroupBox(self.cropTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerCropGroupBox.sizePolicy().hasHeightForWidth())
        self.registerCropGroupBox.setSizePolicy(sizePolicy)
        self.registerCropGroupBox.setMinimumSize(QtCore.QSize(0, 200))
        self.registerCropGroupBox.setMaximumSize(QtCore.QSize(340, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.registerCropGroupBox.setFont(font)
        self.registerCropGroupBox.setObjectName("registerCropGroupBox")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.registerCropGroupBox)
        self.gridLayout_14.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_14.setSpacing(5)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.cropNameLabel = QtWidgets.QLabel(self.registerCropGroupBox)
        self.cropNameLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropNameLabel.setObjectName("cropNameLabel")
        self.horizontalLayout_28.addWidget(self.cropNameLabel)
        self.verticalLayout_11.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.cropNameLineEdit = QtWidgets.QLineEdit(self.registerCropGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropNameLineEdit.sizePolicy().hasHeightForWidth())
        self.cropNameLineEdit.setSizePolicy(sizePolicy)
        self.cropNameLineEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.cropNameLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropNameLineEdit.setObjectName("cropNameLineEdit")
        self.horizontalLayout_29.addWidget(self.cropNameLineEdit)
        self.verticalLayout_11.addLayout(self.horizontalLayout_29)
        self.gridLayout_14.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.cropSowingDateLabel = QtWidgets.QLabel(self.registerCropGroupBox)
        self.cropSowingDateLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropSowingDateLabel.setObjectName("cropSowingDateLabel")
        self.horizontalLayout_19.addWidget(self.cropSowingDateLabel)
        self.cropHarvestingDateLabel = QtWidgets.QLabel(self.registerCropGroupBox)
        self.cropHarvestingDateLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropHarvestingDateLabel.setObjectName("cropHarvestingDateLabel")
        self.horizontalLayout_19.addWidget(self.cropHarvestingDateLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.cropSowingDate = QtWidgets.QDateEdit(self.registerCropGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropSowingDate.sizePolicy().hasHeightForWidth())
        self.cropSowingDate.setSizePolicy(sizePolicy)
        self.cropSowingDate.setMinimumSize(QtCore.QSize(0, 23))
        self.cropSowingDate.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropSowingDate.setCalendarPopup(True)
        self.cropSowingDate.setObjectName("cropSowingDate")
        self.horizontalLayout_25.addWidget(self.cropSowingDate)
        self.cropHarvestingDate = QtWidgets.QDateEdit(self.registerCropGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropHarvestingDate.sizePolicy().hasHeightForWidth())
        self.cropHarvestingDate.setSizePolicy(sizePolicy)
        self.cropHarvestingDate.setMinimumSize(QtCore.QSize(0, 23))
        self.cropHarvestingDate.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropHarvestingDate.setCalendarPopup(True)
        self.cropHarvestingDate.setObjectName("cropHarvestingDate")
        self.horizontalLayout_25.addWidget(self.cropHarvestingDate)
        self.verticalLayout_6.addLayout(self.horizontalLayout_25)
        self.gridLayout_14.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.cropVarietyLabel = QtWidgets.QLabel(self.registerCropGroupBox)
        self.cropVarietyLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropVarietyLabel.setObjectName("cropVarietyLabel")
        self.horizontalLayout_26.addWidget(self.cropVarietyLabel)
        self.cropInterRoCmLabel = QtWidgets.QLabel(self.registerCropGroupBox)
        self.cropInterRoCmLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropInterRoCmLabel.setObjectName("cropInterRoCmLabel")
        self.horizontalLayout_26.addWidget(self.cropInterRoCmLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.cropVarietyLineEdit = QtWidgets.QLineEdit(self.registerCropGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropVarietyLineEdit.sizePolicy().hasHeightForWidth())
        self.cropVarietyLineEdit.setSizePolicy(sizePolicy)
        self.cropVarietyLineEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.cropVarietyLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropVarietyLineEdit.setObjectName("cropVarietyLineEdit")
        self.horizontalLayout_27.addWidget(self.cropVarietyLineEdit)
        self.cropInterRoCMSpinBox = QtWidgets.QDoubleSpinBox(self.registerCropGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropInterRoCMSpinBox.sizePolicy().hasHeightForWidth())
        self.cropInterRoCMSpinBox.setSizePolicy(sizePolicy)
        self.cropInterRoCMSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropInterRoCMSpinBox.setObjectName("cropInterRoCMSpinBox")
        self.horizontalLayout_27.addWidget(self.cropInterRoCMSpinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_27)
        self.gridLayout_14.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.cropIDLabel = QtWidgets.QLabel(self.registerCropGroupBox)
        self.cropIDLabel.setEnabled(True)
        self.cropIDLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropIDLabel.setObjectName("cropIDLabel")
        self.horizontalLayout_14.addWidget(self.cropIDLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.cropAddPushButton = QtWidgets.QPushButton(self.registerCropGroupBox)
        self.cropAddPushButton.setMinimumSize(QtCore.QSize(110, 30))
        self.cropAddPushButton.setMaximumSize(QtCore.QSize(110, 16777215))
        self.cropAddPushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropAddPushButton.setIcon(icon)
        self.cropAddPushButton.setObjectName("cropAddPushButton")
        self.horizontalLayout_14.addWidget(self.cropAddPushButton)
        self.gridLayout_14.addLayout(self.horizontalLayout_14, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.registerCropGroupBox)
        self.manageCropGroupBox = QtWidgets.QGroupBox(self.cropTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manageCropGroupBox.sizePolicy().hasHeightForWidth())
        self.manageCropGroupBox.setSizePolicy(sizePolicy)
        self.manageCropGroupBox.setMinimumSize(QtCore.QSize(0, 85))
        self.manageCropGroupBox.setMaximumSize(QtCore.QSize(340, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.manageCropGroupBox.setFont(font)
        self.manageCropGroupBox.setObjectName("manageCropGroupBox")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.manageCropGroupBox)
        self.gridLayout_13.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_13.setSpacing(5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.cropEditPushButton = QtWidgets.QPushButton(self.manageCropGroupBox)
        self.cropEditPushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.cropEditPushButton.setMaximumSize(QtCore.QSize(110, 30))
        self.cropEditPushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropEditPushButton.setIcon(icon1)
        self.cropEditPushButton.setIconSize(QtCore.QSize(24, 24))
        self.cropEditPushButton.setObjectName("cropEditPushButton")
        self.horizontalLayout_18.addWidget(self.cropEditPushButton)
        self.cropDeletePushButton = QtWidgets.QPushButton(self.manageCropGroupBox)
        self.cropDeletePushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.cropDeletePushButton.setMaximumSize(QtCore.QSize(110, 30))
        self.cropDeletePushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.cropDeletePushButton.setIcon(icon2)
        self.cropDeletePushButton.setIconSize(QtCore.QSize(24, 24))
        self.cropDeletePushButton.setObjectName("cropDeletePushButton")
        self.horizontalLayout_18.addWidget(self.cropDeletePushButton)
        self.gridLayout_13.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.manageCropGroupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.farmerTabWidget.addTab(self.cropTab, "")
        self.gridLayout.addWidget(self.farmerTabWidget, 0, 0, 1, 1)

        self.retranslateUi(FarmerDialog)
        self.farmerTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FarmerDialog)
        FarmerDialog.setTabOrder(self.farmerTabWidget, self.farmerTableWidget)
        FarmerDialog.setTabOrder(self.farmerTableWidget, self.farmerFirstNameLineEdit)
        FarmerDialog.setTabOrder(self.farmerFirstNameLineEdit, self.farmerLastNameLineEdit)
        FarmerDialog.setTabOrder(self.farmerLastNameLineEdit, self.farmerAddressLineEdit)
        FarmerDialog.setTabOrder(self.farmerAddressLineEdit, self.farmerTown)
        FarmerDialog.setTabOrder(self.farmerTown, self.farmerCountry)
        FarmerDialog.setTabOrder(self.farmerCountry, self.farmerZipCode)
        FarmerDialog.setTabOrder(self.farmerZipCode, self.farmerAddPushButton)
        FarmerDialog.setTabOrder(self.farmerAddPushButton, self.farmerEditPushButton)
        FarmerDialog.setTabOrder(self.farmerEditPushButton, self.farmerDeletePushButton)
        FarmerDialog.setTabOrder(self.farmerDeletePushButton, self.cropTableWidget)
        FarmerDialog.setTabOrder(self.cropTableWidget, self.cropNameLineEdit)
        FarmerDialog.setTabOrder(self.cropNameLineEdit, self.cropSowingDate)
        FarmerDialog.setTabOrder(self.cropSowingDate, self.cropHarvestingDate)
        FarmerDialog.setTabOrder(self.cropHarvestingDate, self.cropVarietyLineEdit)
        FarmerDialog.setTabOrder(self.cropVarietyLineEdit, self.cropAddPushButton)
        FarmerDialog.setTabOrder(self.cropAddPushButton, self.cropEditPushButton)
        FarmerDialog.setTabOrder(self.cropEditPushButton, self.cropDeletePushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("FarmerDialog", "FarmerDialog"))
        self.farmersGroupBox.setTitle(_translate("FarmerDialog", "Farmers"))
        self.farmerTableWidget.setSortingEnabled(True)
        item = self.farmerTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FarmerDialog", "Id"))
        item = self.farmerTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FarmerDialog", "First name"))
        item = self.farmerTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FarmerDialog", "Last name"))
        item = self.farmerTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FarmerDialog", "Address"))
        item = self.farmerTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FarmerDialog", "Zipcode"))
        item = self.farmerTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FarmerDialog", "Town"))
        item = self.farmerTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("FarmerDialog", "Country"))
        item = self.farmerTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("FarmerDialog", "Create date"))
        item = self.farmerTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("FarmerDialog", "Update date"))
        self.farmerGroupBox.setTitle(_translate("FarmerDialog", "Add farmer"))
        self.farmerAddressLabel.setText(_translate("FarmerDialog", "Address line"))
        self.farmerTownLabel.setText(_translate("FarmerDialog", "Town"))
        self.farmerCountryLabel.setText(_translate("FarmerDialog", "Country"))
        self.farmerZipcodeLabel.setText(_translate("FarmerDialog", "Zipcode"))
        self.farmerFirstNameLabel.setText(_translate("FarmerDialog", "First name"))
        self.farmerLastNameLabel.setText(_translate("FarmerDialog", "Last name"))
        self.farmerIDLabel.setText(_translate("FarmerDialog", "noid"))
        self.farmerAddPushButton.setText(_translate("FarmerDialog", "  Add"))
        self.farmerManagerGroupBox.setTitle(_translate("FarmerDialog", "Manage farmer"))
        self.farmerEditPushButton.setText(_translate("FarmerDialog", "  Edit"))
        self.farmerDeletePushButton.setText(_translate("FarmerDialog", "  Delete"))
        self.farmerTabWidget.setTabText(self.farmerTabWidget.indexOf(self.farmerTab), _translate("FarmerDialog", "Farmers management"))
        self.cropGroupBox.setTitle(_translate("FarmerDialog", "Crop list"))
        self.cropTableWidget.setSortingEnabled(True)
        item = self.cropTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FarmerDialog", "Id"))
        item = self.cropTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FarmerDialog", "Crop name"))
        item = self.cropTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FarmerDialog", "Sowing date"))
        item = self.cropTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FarmerDialog", "Harvesting date"))
        item = self.cropTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FarmerDialog", "Variety"))
        item = self.cropTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FarmerDialog", "InterRoCM"))
        item = self.cropTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("FarmerDialog", "Create date"))
        item = self.cropTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("FarmerDialog", "Modify date"))
        self.registerCropGroupBox.setTitle(_translate("FarmerDialog", "Add crop"))
        self.cropNameLabel.setText(_translate("FarmerDialog", "Crop name"))
        self.cropSowingDateLabel.setText(_translate("FarmerDialog", "Sowing date"))
        self.cropHarvestingDateLabel.setText(_translate("FarmerDialog", "Harvesting date"))
        self.cropVarietyLabel.setText(_translate("FarmerDialog", "Variety"))
        self.cropInterRoCmLabel.setText(_translate("FarmerDialog", "InterRoCM"))
        self.cropIDLabel.setText(_translate("FarmerDialog", "noid"))
        self.cropAddPushButton.setText(_translate("FarmerDialog", "  Add"))
        self.manageCropGroupBox.setTitle(_translate("FarmerDialog", "Manage crop"))
        self.cropEditPushButton.setText(_translate("FarmerDialog", "  Edit"))
        self.cropDeletePushButton.setText(_translate("FarmerDialog", "  Delete"))
        self.farmerTabWidget.setTabText(self.farmerTabWidget.indexOf(self.cropTab), _translate("FarmerDialog", "Crop management"))
