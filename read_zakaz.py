# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_zakaz.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Read_Zakaz(object):
    def setupUi(self, Read_Zakaz):
        Read_Zakaz.setObjectName("Read_Zakaz")
        Read_Zakaz.resize(652, 516)
        self.verticalLayoutWidget = QtWidgets.QWidget(Read_Zakaz)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 631, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edtFilename = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtFilename.setObjectName("edtFilename")
        self.horizontalLayout.addWidget(self.edtFilename)
        self.btnOpen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lstItems = QtWidgets.QListView(self.verticalLayoutWidget)
        self.lstItems.setObjectName("lstItems")
        self.verticalLayout.addWidget(self.lstItems)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnRead = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnRead.setObjectName("btnRead")
        self.horizontalLayout_3.addWidget(self.btnRead)
        self.btnDel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDel.setObjectName("btnDel")
        self.horizontalLayout_3.addWidget(self.btnDel)
        self.btnClose = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_3.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Read_Zakaz)
        QtCore.QMetaObject.connectSlotsByName(Read_Zakaz)

    def retranslateUi(self, Read_Zakaz):
        _translate = QtCore.QCoreApplication.translate
        Read_Zakaz.setWindowTitle(_translate("Read_Zakaz", "Заказ кодов маркировки"))
        self.label.setText(_translate("Read_Zakaz", "Выберите файл заказа:"))
        self.btnOpen.setText(_translate("Read_Zakaz", "Обзор"))
        self.btnRead.setText(_translate("Read_Zakaz", "Разобрать"))
        self.btnDel.setText(_translate("Read_Zakaz", "Удалить позицию"))
        self.btnClose.setText(_translate("Read_Zakaz", "Закрыть"))
