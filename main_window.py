# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(218, 346)
        self.verticalLayoutWidget = QtWidgets.QWidget(Main_Window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 221, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnOrders = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnOrders.setObjectName("btnOrders")
        self.verticalLayout.addWidget(self.btnOrders)
        self.btnPrintDatamatrix = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPrintDatamatrix.setObjectName("btnPrintDatamatrix")
        self.verticalLayout.addWidget(self.btnPrintDatamatrix)
        self.btnPrintSSCC = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPrintSSCC.setObjectName("btnPrintSSCC")
        self.verticalLayout.addWidget(self.btnPrintSSCC)
        self.btnAgregation = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAgregation.setObjectName("btnAgregation")
        self.verticalLayout.addWidget(self.btnAgregation)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.btnClose = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout.addWidget(self.btnClose)

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "Маркировка кодами ЧЕСТНЫЙ ЗНАК"))
        self.btnOrders.setText(_translate("Main_Window", "Обработка заказов"))
        self.btnPrintDatamatrix.setText(_translate("Main_Window", "Печать этикеток с кодами DataMatrix"))
        self.btnPrintSSCC.setText(_translate("Main_Window", "Печать штрихкодов для коробов"))
        self.btnAgregation.setText(_translate("Main_Window", "Агрегация в короба"))
        self.pushButton_6.setText(_translate("Main_Window", "PushButton"))
        self.pushButton_7.setText(_translate("Main_Window", "PushButton"))
        self.btnClose.setText(_translate("Main_Window", "Выход"))
