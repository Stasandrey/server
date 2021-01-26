# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print_codes.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Print_Codes(object):
    def setupUi(self, Print_Codes):
        Print_Codes.setObjectName("Print_Codes")
        Print_Codes.resize(321, 175)
        self.verticalLayoutWidget = QtWidgets.QWidget(Print_Codes)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 321, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.cmbModel = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmbModel.setObjectName("cmbModel")
        self.verticalLayout_2.addWidget(self.cmbModel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.cmbSize = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmbSize.setObjectName("cmbSize")
        self.verticalLayout_3.addWidget(self.cmbSize)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lblGtin = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblGtin.setText("")
        self.lblGtin.setObjectName("lblGtin")
        self.verticalLayout.addWidget(self.lblGtin)
        self.lblNumber = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblNumber.setText("")
        self.lblNumber.setObjectName("lblNumber")
        self.verticalLayout.addWidget(self.lblNumber)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.spnNumber = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spnNumber.setObjectName("spnNumber")
        self.verticalLayout.addWidget(self.spnNumber)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnPrint = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPrint.setObjectName("btnPrint")
        self.horizontalLayout_2.addWidget(self.btnPrint)
        self.btnSetup = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSetup.setObjectName("btnSetup")
        self.horizontalLayout_2.addWidget(self.btnSetup)
        self.btnClose = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Print_Codes)
        QtCore.QMetaObject.connectSlotsByName(Print_Codes)

    def retranslateUi(self, Print_Codes):
        _translate = QtCore.QCoreApplication.translate
        Print_Codes.setWindowTitle(_translate("Print_Codes", "Печать этикеток с кодами маркировки"))
        self.label.setText(_translate("Print_Codes", "Модель"))
        self.label_2.setText(_translate("Print_Codes", "Размер"))
        self.label_4.setText(_translate("Print_Codes", "Количество этикеток для печати:"))
        self.btnPrint.setText(_translate("Print_Codes", "Печать"))
        self.btnSetup.setText(_translate("Print_Codes", "Настройка принтера"))
        self.btnClose.setText(_translate("Print_Codes", "Выход"))
