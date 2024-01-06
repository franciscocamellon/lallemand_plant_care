# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treatment_polygons_dlg_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TreatmentPolygonsDialogBase(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 445)
        Dialog.setMinimumSize(QtCore.QSize(465, 445))
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 10, -1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gpsPointLayerLabel = QtWidgets.QLabel(self.tab)
        self.gpsPointLayerLabel.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gpsPointLayerLabel.setFont(font)
        self.gpsPointLayerLabel.setStyleSheet("")
        self.gpsPointLayerLabel.setObjectName("gpsPointLayerLabel")
        self.horizontalLayout.addWidget(self.gpsPointLayerLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gpsPointLayerComboBox = QgsMapLayerComboBox(self.tab)
        self.gpsPointLayerComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.gpsPointLayerComboBox.setObjectName("gpsPointLayerComboBox")
        self.horizontalLayout_2.addWidget(self.gpsPointLayerComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.crsLabel = QtWidgets.QLabel(self.tab)
        self.crsLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.crsLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.crsLabel.setObjectName("crsLabel")
        self.horizontalLayout_5.addWidget(self.crsLabel)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.crsWarningLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.crsWarningLabel.setFont(font)
        self.crsWarningLabel.setStyleSheet("")
        self.crsWarningLabel.setObjectName("crsWarningLabel")
        self.horizontalLayout_5.addWidget(self.crsWarningLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.reprojectCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.reprojectCheckBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.reprojectCheckBox.setObjectName("reprojectCheckBox")
        self.horizontalLayout_3.addWidget(self.reprojectCheckBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.suggestedCrsSelectionWidget = QgsProjectionSelectionWidget(self.groupBox)
        self.suggestedCrsSelectionWidget.setMinimumSize(QtCore.QSize(0, 23))
        self.suggestedCrsSelectionWidget.setMaximumSize(QtCore.QSize(16777215, 23))
        self.suggestedCrsSelectionWidget.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.suggestedCrsSelectionWidget.setObjectName("suggestedCrsSelectionWidget")
        self.horizontalLayout_4.addWidget(self.suggestedCrsSelectionWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 4, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.treatmentCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.treatmentCheckBox.setMinimumSize(QtCore.QSize(0, 17))
        self.treatmentCheckBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.treatmentCheckBox.setObjectName("treatmentCheckBox")
        self.horizontalLayout_8.addWidget(self.treatmentCheckBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(10, 0, -1, -1)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.methodLabel = QtWidgets.QLabel(self.groupBox)
        self.methodLabel.setMinimumSize(QtCore.QSize(0, 17))
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
        self.sortingLabel = QtWidgets.QLabel(self.groupBox)
        self.sortingLabel.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sortingLabel.setFont(font)
        self.sortingLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sortingLabel.setObjectName("sortingLabel")
        self.horizontalLayout_17.addWidget(self.sortingLabel)
        self.borderSizeLabel = QtWidgets.QLabel(self.groupBox)
        self.borderSizeLabel.setMinimumSize(QtCore.QSize(0, 17))
        self.borderSizeLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.borderSizeLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.borderSizeLabel.setObjectName("borderSizeLabel")
        self.horizontalLayout_17.addWidget(self.borderSizeLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_18.setSpacing(7)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.methodComboBox = QtWidgets.QComboBox(self.groupBox)
        self.methodComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.methodComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.methodComboBox.setObjectName("methodComboBox")
        self.horizontalLayout_18.addWidget(self.methodComboBox)
        self.sortingFieldComboBox = QgsFieldComboBox(self.groupBox)
        self.sortingFieldComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.sortingFieldComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.sortingFieldComboBox.setObjectName("sortingFieldComboBox")
        self.horizontalLayout_18.addWidget(self.sortingFieldComboBox)
        self.borderSizeSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.borderSizeSpinBox.setMinimumSize(QtCore.QSize(0, 23))
        self.borderSizeSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.borderSizeSpinBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.borderSizeSpinBox.setObjectName("borderSizeSpinBox")
        self.horizontalLayout_18.addWidget(self.borderSizeSpinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_18)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, 5, -1, -1)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.boundaryCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.boundaryCheckBox.setMinimumSize(QtCore.QSize(0, 17))
        self.boundaryCheckBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.boundaryCheckBox.setObjectName("boundaryCheckBox")
        self.horizontalLayout_6.addWidget(self.boundaryCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem6, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.createPolygonsPushButton = QtWidgets.QPushButton(self.tab)
        self.createPolygonsPushButton.setMinimumSize(QtCore.QSize(100, 23))
        self.createPolygonsPushButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.createPolygonsPushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.createPolygonsPushButton.setObjectName("createPolygonsPushButton")
        self.horizontalLayout_7.addWidget(self.createPolygonsPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.gpsPointLayerLabel.setText(_translate("Dialog", "Gps points layer"))
        self.crsLabel.setText(_translate("Dialog", "CRS -> "))
        self.crsWarningLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:8pt; color:#ff0000;\">**Needs to be reprojected</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Dialog", "Actions"))
        self.reprojectCheckBox.setText(_translate("Dialog", "Reprojection"))
        self.label.setText(_translate("Dialog", "Suggested CRS:"))
        self.treatmentCheckBox.setText(_translate("Dialog", "Create treatment polygons"))
        self.methodLabel.setText(_translate("Dialog", "Method"))
        self.sortingLabel.setText(_translate("Dialog", "Sorting variable"))
        self.borderSizeLabel.setText(_translate("Dialog", "Border size"))
        self.boundaryCheckBox.setText(_translate("Dialog", "Create boundary polygon"))
        self.createPolygonsPushButton.setText(_translate("Dialog", "Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Treatments"))
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
