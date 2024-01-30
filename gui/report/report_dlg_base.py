# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report_dlg_base.ui'
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
        self.tabWidget.setObjectName("tabWidget")
        self.reportTab = QtWidgets.QWidget()
        self.reportTab.setObjectName("reportTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.reportTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.parametersGroupBox = QtWidgets.QGroupBox(self.reportTab)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gainSurfacePointsLabel = QtWidgets.QLabel(self.parametersGroupBox)
        self.gainSurfacePointsLabel.setMinimumSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gainSurfacePointsLabel.setFont(font)
        self.gainSurfacePointsLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.gainSurfacePointsLabel.setObjectName("gainSurfacePointsLabel")
        self.horizontalLayout_3.addWidget(self.gainSurfacePointsLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gainSurfacePointsComboBox = QgsMapLayerComboBox(self.parametersGroupBox)
        self.gainSurfacePointsComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.gainSurfacePointsComboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gainSurfacePointsComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.gainSurfacePointsComboBox.setObjectName("gainSurfacePointsComboBox")
        self.horizontalLayout_4.addWidget(self.gainSurfacePointsComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.t1FinalSurfaceLabel = QtWidgets.QLabel(self.parametersGroupBox)
        self.t1FinalSurfaceLabel.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.t1FinalSurfaceLabel.setFont(font)
        self.t1FinalSurfaceLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.t1FinalSurfaceLabel.setObjectName("t1FinalSurfaceLabel")
        self.horizontalLayout_10.addWidget(self.t1FinalSurfaceLabel)
        self.t2FinalSurfaceLabel = QtWidgets.QLabel(self.parametersGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2FinalSurfaceLabel.sizePolicy().hasHeightForWidth())
        self.t2FinalSurfaceLabel.setSizePolicy(sizePolicy)
        self.t2FinalSurfaceLabel.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.t2FinalSurfaceLabel.setFont(font)
        self.t2FinalSurfaceLabel.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.t2FinalSurfaceLabel.setObjectName("t2FinalSurfaceLabel")
        self.horizontalLayout_10.addWidget(self.t2FinalSurfaceLabel)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_11.setSpacing(8)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.t1SurfacePointsComboBox = QgsMapLayerComboBox(self.parametersGroupBox)
        self.t1SurfacePointsComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.t1SurfacePointsComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.t1SurfacePointsComboBox.setObjectName("t1SurfacePointsComboBox")
        self.horizontalLayout_11.addWidget(self.t1SurfacePointsComboBox)
        self.t2SurfacePointsComboBox = QgsMapLayerComboBox(self.parametersGroupBox)
        self.t2SurfacePointsComboBox.setMinimumSize(QtCore.QSize(0, 23))
        self.t2SurfacePointsComboBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\"")
        self.t2SurfacePointsComboBox.setObjectName("t2SurfacePointsComboBox")
        self.horizontalLayout_11.addWidget(self.t2SurfacePointsComboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_3.addLayout(self.verticalLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.reportPushButton = QtWidgets.QPushButton(self.parametersGroupBox)
        self.reportPushButton.setMinimumSize(QtCore.QSize(100, 23))
        self.reportPushButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.reportPushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.reportPushButton.setObjectName("reportPushButton")
        self.horizontalLayout_7.addWidget(self.reportPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.gridLayout_2.addWidget(self.parametersGroupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.reportTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.parametersGroupBox.setTitle(_translate("Dialog", "Parameters"))
        self.gainSurfacePointsLabel.setText(_translate("Dialog", "Gain surface points"))
        self.t1FinalSurfaceLabel.setText(_translate("Dialog", "T1 final surface points"))
        self.t2FinalSurfaceLabel.setText(_translate("Dialog", "T2 final surface points"))
        self.reportPushButton.setText(_translate("Dialog", "Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reportTab), _translate("Dialog", "Report"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
