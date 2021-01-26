# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print_SSCC.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Print_SSCC(object):
    def setupUi(self, Print_SSCC):
        Print_SSCC.setObjectName("Print_SSCC")
        Print_SSCC.resize(330, 262)
        self.verticalLayoutWidget = QtWidgets.QWidget(Print_SSCC)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spnNumber = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spnNumber.setMaximum(10000)
        self.spnNumber.setObjectName("spnNumber")
        self.verticalLayout.addWidget(self.spnNumber)
        self.lblWork = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblWork.setText("")
        self.lblWork.setObjectName("lblWork")
        self.verticalLayout.addWidget(self.lblWork)
        self.prgBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.prgBar.setEnabled(True)
        self.prgBar.setProperty("value", 0)
        self.prgBar.setTextVisible(True)
        self.prgBar.setInvertedAppearance(False)
        self.prgBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.prgBar.setObjectName("prgBar")
        self.verticalLayout.addWidget(self.prgBar)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPrint = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPrint.setObjectName("btnPrint")
        self.horizontalLayout.addWidget(self.btnPrint)
        self.btnSetup = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSetup.setObjectName("btnSetup")
        self.horizontalLayout.addWidget(self.btnSetup)
        self.btnClose = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Print_SSCC)
        QtCore.QMetaObject.connectSlotsByName(Print_SSCC)

    def retranslateUi(self, Print_SSCC):
        _translate = QtCore.QCoreApplication.translate
        Print_SSCC.setWindowTitle(_translate("Print_SSCC", "Печать SSCC для агрегации"))
        self.label.setText(_translate("Print_SSCC", "Количество SSCC кодов:"))
        self.btnPrint.setText(_translate("Print_SSCC", "Печать"))
        self.btnSetup.setText(_translate("Print_SSCC", "Настройки принтера"))
        self.btnClose.setText(_translate("Print_SSCC", "Выход"))
