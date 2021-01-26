# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_codes.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Read_Codes(object):
    def setupUi(self, Read_Codes):
        Read_Codes.setObjectName("Read_Codes")
        Read_Codes.resize(761, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Read_Codes)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.edtCode = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtCode.setObjectName("edtCode")
        self.verticalLayout.addWidget(self.edtCode)
        self.lblKorob = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblKorob.setText("")
        self.lblKorob.setObjectName("lblKorob")
        self.verticalLayout.addWidget(self.lblKorob)
        self.lstInside = QtWidgets.QListView(self.verticalLayoutWidget)
        self.lstInside.setObjectName("lstInside")
        self.verticalLayout.addWidget(self.lstInside)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnClear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        self.btnGenerateAgr = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnGenerateAgr.setObjectName("btnGenerateAgr")
        self.horizontalLayout.addWidget(self.btnGenerateAgr)
        self.btnClose = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Read_Codes)
        QtCore.QMetaObject.connectSlotsByName(Read_Codes)

    def retranslateUi(self, Read_Codes):
        _translate = QtCore.QCoreApplication.translate
        Read_Codes.setWindowTitle(_translate("Read_Codes", "Считывание штрих-кодов"))
        self.label.setText(_translate("Read_Codes", "Введенный код:"))
        self.btnClear.setText(_translate("Read_Codes", "Очистить"))
        self.btnGenerateAgr.setText(_translate("Read_Codes", "Сформировать файл агрегации"))
        self.btnClose.setText(_translate("Read_Codes", "Выход"))
