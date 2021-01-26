# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_datamatrix_stickers.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Read_Datamatrix_Stickers(object):
    def setupUi(self, Read_Datamatrix_Stickers):
        Read_Datamatrix_Stickers.setObjectName("Read_Datamatrix_Stickers")
        Read_Datamatrix_Stickers.resize(332, 341)
        self.verticalLayoutWidget = QtWidgets.QWidget(Read_Datamatrix_Stickers)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edtFiles = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtFiles.setObjectName("edtFiles")
        self.horizontalLayout.addWidget(self.edtFiles)
        self.btnOpen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.prgAll = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.prgAll.setProperty("value", 0)
        self.prgAll.setObjectName("prgAll")
        self.verticalLayout.addWidget(self.prgAll)
        self.lblFile = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblFile.setText("")
        self.lblFile.setObjectName("lblFile")
        self.verticalLayout.addWidget(self.lblFile)
        self.prgFile = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.prgFile.setProperty("value", 0)
        self.prgFile.setObjectName("prgFile")
        self.verticalLayout.addWidget(self.prgFile)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnWork = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnWork.setObjectName("btnWork")
        self.horizontalLayout_2.addWidget(self.btnWork)
        self.btnClose = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Read_Datamatrix_Stickers)
        QtCore.QMetaObject.connectSlotsByName(Read_Datamatrix_Stickers)

    def retranslateUi(self, Read_Datamatrix_Stickers):
        _translate = QtCore.QCoreApplication.translate
        Read_Datamatrix_Stickers.setWindowTitle(_translate("Read_Datamatrix_Stickers", "Разбор файлов заказа кодов маркировки"))
        self.label.setText(_translate("Read_Datamatrix_Stickers", "Выберите файлы заказов:"))
        self.btnOpen.setText(_translate("Read_Datamatrix_Stickers", "..."))
        self.label_2.setText(_translate("Read_Datamatrix_Stickers", "Общий ход выполнения:"))
        self.btnWork.setText(_translate("Read_Datamatrix_Stickers", "Разобрать"))
        self.btnClose.setText(_translate("Read_Datamatrix_Stickers", "Выход"))
