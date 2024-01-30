# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_settings_dlg_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 610)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.mGroupBox_3 = QgsCollapsibleGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mGroupBox_3.sizePolicy().hasHeightForWidth())
        self.mGroupBox_3.setSizePolicy(sizePolicy)
        self.mGroupBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.mGroupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mGroupBox_3.setObjectName("mGroupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mGroupBox_3)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.fieldToInterpolateLabel = QtWidgets.QLabel(self.mGroupBox_3)
        self.fieldToInterpolateLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.fieldToInterpolateLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.fieldToInterpolateLabel.setObjectName("fieldToInterpolateLabel")
        self.horizontalLayout_15.addWidget(self.fieldToInterpolateLabel)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.fieldToInterpolateLineEdit = QtWidgets.QLineEdit(self.mGroupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldToInterpolateLineEdit.sizePolicy().hasHeightForWidth())
        self.fieldToInterpolateLineEdit.setSizePolicy(sizePolicy)
        self.fieldToInterpolateLineEdit.setMinimumSize(QtCore.QSize(165, 18))
        self.fieldToInterpolateLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.fieldToInterpolateLineEdit.setObjectName("fieldToInterpolateLineEdit")
        self.horizontalLayout_15.addWidget(self.fieldToInterpolateLineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pixelSizeXLabel = QtWidgets.QLabel(self.mGroupBox_3)
        self.pixelSizeXLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.pixelSizeXLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.pixelSizeXLabel.setObjectName("pixelSizeXLabel")
        self.horizontalLayout_16.addWidget(self.pixelSizeXLabel)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.pixelSizeXSpinBox = QtWidgets.QDoubleSpinBox(self.mGroupBox_3)
        self.pixelSizeXSpinBox.setMinimumSize(QtCore.QSize(165, 18))
        self.pixelSizeXSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.pixelSizeXSpinBox.setDecimals(4)
        self.pixelSizeXSpinBox.setMaximum(999.99)
        self.pixelSizeXSpinBox.setSingleStep(0.1)
        self.pixelSizeXSpinBox.setProperty("value", 1.5)
        self.pixelSizeXSpinBox.setObjectName("pixelSizeXSpinBox")
        self.horizontalLayout_16.addWidget(self.pixelSizeXSpinBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pixelSizeYLabel = QtWidgets.QLabel(self.mGroupBox_3)
        self.pixelSizeYLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.pixelSizeYLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.pixelSizeYLabel.setObjectName("pixelSizeYLabel")
        self.horizontalLayout_17.addWidget(self.pixelSizeYLabel)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem4)
        self.pixelSizeYSpinBox = QtWidgets.QDoubleSpinBox(self.mGroupBox_3)
        self.pixelSizeYSpinBox.setMinimumSize(QtCore.QSize(165, 18))
        self.pixelSizeYSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.pixelSizeYSpinBox.setDecimals(4)
        self.pixelSizeYSpinBox.setMinimum(0.0)
        self.pixelSizeYSpinBox.setMaximum(999.99)
        self.pixelSizeYSpinBox.setSingleStep(0.1)
        self.pixelSizeYSpinBox.setProperty("value", 1.5)
        self.pixelSizeYSpinBox.setObjectName("pixelSizeYSpinBox")
        self.horizontalLayout_17.addWidget(self.pixelSizeYSpinBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.gridLayout.addWidget(self.mGroupBox_3, 2, 0, 1, 1)
        self.mGroupBox_4 = QgsCollapsibleGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mGroupBox_4.sizePolicy().hasHeightForWidth())
        self.mGroupBox_4.setSizePolicy(sizePolicy)
        self.mGroupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.mGroupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mGroupBox_4.setObjectName("mGroupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.mGroupBox_4)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.binsLabel = QtWidgets.QLabel(self.mGroupBox_4)
        self.binsLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.binsLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.binsLabel.setObjectName("binsLabel")
        self.horizontalLayout_18.addWidget(self.binsLabel)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem6)
        self.binsSpinBox = QtWidgets.QSpinBox(self.mGroupBox_4)
        self.binsSpinBox.setMinimumSize(QtCore.QSize(165, 18))
        self.binsSpinBox.setObjectName("binsSpinBox")
        self.horizontalLayout_18.addWidget(self.binsSpinBox)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.colorLabel = QtWidgets.QLabel(self.mGroupBox_4)
        self.colorLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.colorLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.colorLabel.setObjectName("colorLabel")
        self.horizontalLayout_19.addWidget(self.colorLabel)
        spacerItem8 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem8)
        self.colorColorButton = QgsColorButton(self.mGroupBox_4)
        self.colorColorButton.setMinimumSize(QtCore.QSize(165, 18))
        self.colorColorButton.setObjectName("colorColorButton")
        self.horizontalLayout_19.addWidget(self.colorColorButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem9)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.edgeColorLabel = QtWidgets.QLabel(self.mGroupBox_4)
        self.edgeColorLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.edgeColorLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.edgeColorLabel.setObjectName("edgeColorLabel")
        self.horizontalLayout_20.addWidget(self.edgeColorLabel)
        spacerItem10 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem10)
        self.edgeColorButton = QgsColorButton(self.mGroupBox_4)
        self.edgeColorButton.setMinimumSize(QtCore.QSize(165, 18))
        self.edgeColorButton.setObjectName("edgeColorButton")
        self.horizontalLayout_20.addWidget(self.edgeColorButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_20)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.gridLayout.addWidget(self.mGroupBox_4, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 4, 0, 1, 1)
        self.mGroupBox_2 = QgsCollapsibleGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mGroupBox_2.sizePolicy().hasHeightForWidth())
        self.mGroupBox_2.setSizePolicy(sizePolicy)
        self.mGroupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.mGroupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mGroupBox_2.setObjectName("mGroupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.oddPolygonsLabel = QtWidgets.QLabel(self.mGroupBox_2)
        self.oddPolygonsLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.oddPolygonsLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.oddPolygonsLabel.setObjectName("oddPolygonsLabel")
        self.horizontalLayout_14.addWidget(self.oddPolygonsLabel)
        spacerItem13 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.oddPolygonsNameLineEdit = QtWidgets.QLineEdit(self.mGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oddPolygonsNameLineEdit.sizePolicy().hasHeightForWidth())
        self.oddPolygonsNameLineEdit.setSizePolicy(sizePolicy)
        self.oddPolygonsNameLineEdit.setMinimumSize(QtCore.QSize(165, 18))
        self.oddPolygonsNameLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.oddPolygonsNameLineEdit.setObjectName("oddPolygonsNameLineEdit")
        self.horizontalLayout_14.addWidget(self.oddPolygonsNameLineEdit)
        spacerItem14 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem14)
        self.sortingLabel_6 = QtWidgets.QLabel(self.mGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortingLabel_6.sizePolicy().hasHeightForWidth())
        self.sortingLabel_6.setSizePolicy(sizePolicy)
        self.sortingLabel_6.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sortingLabel_6.setFont(font)
        self.sortingLabel_6.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sortingLabel_6.setObjectName("sortingLabel_6")
        self.horizontalLayout_14.addWidget(self.sortingLabel_6)
        spacerItem15 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem15)
        self.largeurCoupeSpinBox = QtWidgets.QDoubleSpinBox(self.mGroupBox_2)
        self.largeurCoupeSpinBox.setMinimumSize(QtCore.QSize(165, 18))
        self.largeurCoupeSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.largeurCoupeSpinBox.setDecimals(4)
        self.largeurCoupeSpinBox.setObjectName("largeurCoupeSpinBox")
        self.horizontalLayout_14.addWidget(self.largeurCoupeSpinBox)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.evenPolygonsLabel = QtWidgets.QLabel(self.mGroupBox_2)
        self.evenPolygonsLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.evenPolygonsLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.evenPolygonsLabel.setObjectName("evenPolygonsLabel")
        self.horizontalLayout_12.addWidget(self.evenPolygonsLabel)
        spacerItem17 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem17)
        self.evenPolygonsNameLineEdit = QtWidgets.QLineEdit(self.mGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.evenPolygonsNameLineEdit.sizePolicy().hasHeightForWidth())
        self.evenPolygonsNameLineEdit.setSizePolicy(sizePolicy)
        self.evenPolygonsNameLineEdit.setMinimumSize(QtCore.QSize(165, 18))
        self.evenPolygonsNameLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.evenPolygonsNameLineEdit.setObjectName("evenPolygonsNameLineEdit")
        self.horizontalLayout_12.addWidget(self.evenPolygonsNameLineEdit)
        spacerItem18 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem18)
        self.label_3 = QtWidgets.QLabel(self.mGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        spacerItem19 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem19)
        self.sousEchantillonnageSpinBox = QtWidgets.QDoubleSpinBox(self.mGroupBox_2)
        self.sousEchantillonnageSpinBox.setMinimumSize(QtCore.QSize(165, 18))
        self.sousEchantillonnageSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sousEchantillonnageSpinBox.setDecimals(4)
        self.sousEchantillonnageSpinBox.setMinimum(1.0)
        self.sousEchantillonnageSpinBox.setObjectName("sousEchantillonnageSpinBox")
        self.horizontalLayout_12.addWidget(self.sousEchantillonnageSpinBox)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem20)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.evenPolygonsLabel_2 = QtWidgets.QLabel(self.mGroupBox_2)
        self.evenPolygonsLabel_2.setMinimumSize(QtCore.QSize(100, 0))
        self.evenPolygonsLabel_2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.evenPolygonsLabel_2.setObjectName("evenPolygonsLabel_2")
        self.horizontalLayout.addWidget(self.evenPolygonsLabel_2)
        spacerItem21 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem21)
        self.sizeBorderSpinBox = QtWidgets.QDoubleSpinBox(self.mGroupBox_2)
        self.sizeBorderSpinBox.setMinimumSize(QtCore.QSize(165, 18))
        self.sizeBorderSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sizeBorderSpinBox.setDecimals(4)
        self.sizeBorderSpinBox.setMinimum(0.0)
        self.sizeBorderSpinBox.setMaximum(1000.0)
        self.sizeBorderSpinBox.setProperty("value", 0.0)
        self.sizeBorderSpinBox.setObjectName("sizeBorderSpinBox")
        self.horizontalLayout.addWidget(self.sizeBorderSpinBox)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem22)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.mGroupBox_2, 1, 0, 1, 1)
        self.mGroupBox = QgsCollapsibleGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mGroupBox.sizePolicy().hasHeightForWidth())
        self.mGroupBox.setSizePolicy(sizePolicy)
        self.mGroupBox.setMinimumSize(QtCore.QSize(0, 125))
        self.mGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mGroupBox.setObjectName("mGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.databaseNameLabel_2 = QtWidgets.QLabel(self.mGroupBox)
        self.databaseNameLabel_2.setMinimumSize(QtCore.QSize(100, 0))
        self.databaseNameLabel_2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.databaseNameLabel_2.setObjectName("databaseNameLabel_2")
        self.horizontalLayout_13.addWidget(self.databaseNameLabel_2)
        spacerItem23 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem23)
        self.databaseNameLineEdit = QtWidgets.QLineEdit(self.mGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.databaseNameLineEdit.sizePolicy().hasHeightForWidth())
        self.databaseNameLineEdit.setSizePolicy(sizePolicy)
        self.databaseNameLineEdit.setMinimumSize(QtCore.QSize(165, 18))
        self.databaseNameLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.databaseNameLineEdit.setObjectName("databaseNameLineEdit")
        self.horizontalLayout_13.addWidget(self.databaseNameLineEdit)
        spacerItem24 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem24)
        self.serverUserLabel = QtWidgets.QLabel(self.mGroupBox)
        self.serverUserLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.serverUserLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.serverUserLabel.setObjectName("serverUserLabel")
        self.horizontalLayout_13.addWidget(self.serverUserLabel)
        spacerItem25 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem25)
        self.serverUserLineEdit = QtWidgets.QLineEdit(self.mGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverUserLineEdit.sizePolicy().hasHeightForWidth())
        self.serverUserLineEdit.setSizePolicy(sizePolicy)
        self.serverUserLineEdit.setMinimumSize(QtCore.QSize(165, 18))
        self.serverUserLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.serverUserLineEdit.setObjectName("serverUserLineEdit")
        self.horizontalLayout_13.addWidget(self.serverUserLineEdit)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem26)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.serverIpLabel = QtWidgets.QLabel(self.mGroupBox)
        self.serverIpLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.serverIpLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.serverIpLabel.setObjectName("serverIpLabel")
        self.horizontalLayout_8.addWidget(self.serverIpLabel)
        spacerItem27 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem27)
        self.serverIpLineEdit = QtWidgets.QLineEdit(self.mGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverIpLineEdit.sizePolicy().hasHeightForWidth())
        self.serverIpLineEdit.setSizePolicy(sizePolicy)
        self.serverIpLineEdit.setMinimumSize(QtCore.QSize(165, 18))
        self.serverIpLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.serverIpLineEdit.setObjectName("serverIpLineEdit")
        self.horizontalLayout_8.addWidget(self.serverIpLineEdit)
        spacerItem28 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem28)
        self.serverPasswordLabel = QtWidgets.QLabel(self.mGroupBox)
        self.serverPasswordLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.serverPasswordLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.serverPasswordLabel.setObjectName("serverPasswordLabel")
        self.horizontalLayout_8.addWidget(self.serverPasswordLabel)
        spacerItem29 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem29)
        self.serverPasswordLineEdit = QtWidgets.QLineEdit(self.mGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.serverPasswordLineEdit.setSizePolicy(sizePolicy)
        self.serverPasswordLineEdit.setMinimumSize(QtCore.QSize(165, 18))
        self.serverPasswordLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.serverPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.serverPasswordLineEdit.setObjectName("serverPasswordLineEdit")
        self.horizontalLayout_8.addWidget(self.serverPasswordLineEdit)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem30)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.serverPortLabel = QtWidgets.QLabel(self.mGroupBox)
        self.serverPortLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.serverPortLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.serverPortLabel.setObjectName("serverPortLabel")
        self.horizontalLayout_9.addWidget(self.serverPortLabel)
        spacerItem31 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem31)
        self.serverPortLineEdit = QtWidgets.QLineEdit(self.mGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverPortLineEdit.sizePolicy().hasHeightForWidth())
        self.serverPortLineEdit.setSizePolicy(sizePolicy)
        self.serverPortLineEdit.setMinimumSize(QtCore.QSize(165, 18))
        self.serverPortLineEdit.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.serverPortLineEdit.setObjectName("serverPortLineEdit")
        self.horizontalLayout_9.addWidget(self.serverPortLineEdit)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem32)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addWidget(self.mGroupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.mGroupBox_2, self.oddPolygonsNameLineEdit)
        Form.setTabOrder(self.oddPolygonsNameLineEdit, self.evenPolygonsNameLineEdit)
        Form.setTabOrder(self.evenPolygonsNameLineEdit, self.mGroupBox_3)
        Form.setTabOrder(self.mGroupBox_3, self.fieldToInterpolateLineEdit)
        Form.setTabOrder(self.fieldToInterpolateLineEdit, self.pixelSizeXSpinBox)
        Form.setTabOrder(self.pixelSizeXSpinBox, self.pixelSizeYSpinBox)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mGroupBox_3.setTitle(_translate("Form", "Kriging parameters"))
        self.fieldToInterpolateLabel.setText(_translate("Form", "Field to interpolate"))
        self.pixelSizeXLabel.setText(_translate("Form", "Pixel size X"))
        self.pixelSizeYLabel.setText(_translate("Form", "Pixel size Y"))
        self.mGroupBox_4.setTitle(_translate("Form", "Frequency histograms settings"))
        self.binsLabel.setText(_translate("Form", "Bins"))
        self.colorLabel.setText(_translate("Form", "Color"))
        self.edgeColorLabel.setText(_translate("Form", "Edge color"))
        self.mGroupBox_2.setTitle(_translate("Form", "Treatment polygons settings"))
        self.oddPolygonsLabel.setText(_translate("Form", "Odd polygons name"))
        self.sortingLabel_6.setText(_translate("Form", "Largeur coupe"))
        self.evenPolygonsLabel.setText(_translate("Form", "Even polygons name"))
        self.label_3.setText(_translate("Form", "Sous Echantillonnage"))
        self.evenPolygonsLabel_2.setText(_translate("Form", "Border size"))
        self.mGroupBox.setTitle(_translate("Form", "Postgres server settings"))
        self.databaseNameLabel_2.setText(_translate("Form", "Database name"))
        self.serverUserLabel.setText(_translate("Form", "Username"))
        self.serverIpLabel.setText(_translate("Form", "Server IP address"))
        self.serverPasswordLabel.setText(_translate("Form", "Password"))
        self.serverPortLabel.setText(_translate("Form", "Port"))
from qgscollapsiblegroupbox import QgsCollapsibleGroupBox
from qgscolorbutton import QgsColorButton

