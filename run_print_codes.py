#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
import print_codes
#from wand.image import Image
#import sqlite3
#import os
#import time
import dif_func

DBname = 'DB'

class Print_Codes_Window( QtWidgets.QWidget, 
                                            print_codes.Ui_Print_Codes ):
    def __init__( self, database, parent = None   ):
        QtWidgets.QWidget.__init__( self, parent )
        self.setupUi( self )
        self.cmbModel.activated.connect( self.readSizes )
        self.cmbSize.activated.connect( self.calculateCodes )

        self.printer = QtPrintSupport.QPrinter()
        self.printer.setResolution( 203 )

        self.btnPrint.clicked.connect( self.btn_print )
        self.btnSetup.clicked.connect( self.btn_setup )
        self.btnClose.clicked.connect( self.close )
        self.readModels( DBname )
        self.readSizes()
        self.calculateCodes()
#        self.readSizes( DBname )

    def btn_print( self ):
        if self.spnNumber.value() > 0:
#            self.lblWork.setText( "Генерация кодов SSCC" )
#            codes = SSCC_generator.generateSSCC( self.database, 
#                                                                    self.commonPart, 
#                                                                    self.spnNumber.value() )
#            self.lblWork.setText( "Генерация изображений и печать." )
#            self.prgBar.setMaximum( self.spnNumber.value() )
            codes = dif_func.readCodesByGtin( DBname,  self.GTIN )
            print( codes )
            i = 0;
            printed = []
            painter = QtGui.QPainter()
            painter.begin( self.printer )
            while i < self.spnNumber.value():
                pixmap = QtGui.QPixmap( "images\%s.png"%( codes[i][2] ) )
                pixmap = pixmap.scaled( self.printer.width(), 
                                        self.printer.height(), 
                                        aspectRatioMode = QtCore.Qt.KeepAspectRatio )
                painter.drawPixmap( 0, 0, pixmap )
                printed.append( codes[i] )
                i = i + 1
                if i < self.spnNumber.value():
                    self.printer.newPage()
            painter.end()
            dif_func.markCodesPrinted( DBname, printed )
            self.close()
    
    def btn_setup( self ):
        setup = QtPrintSupport.QPrintDialog( self.printer, self )
        setup.setOption( QtPrintSupport.QAbstractPrintDialog.PrintToFile,
                                   on=False )
        setup.setOption( QtPrintSupport.QAbstractPrintDialog.PrintPageRange, 
                                    on=False )
        setup.setOption( QtPrintSupport.QAbstractPrintDialog.PrintCollateCopies, 
                                    on=False )
        setup.setOption( QtPrintSupport.QAbstractPrintDialog.PrintCurrentPage, 
                                    on=False )
        setup.exec()

    def calculateCodes( self ):
        self.GTIN = dif_func.readGtinByModelSize( DBname,  
                    self.cmbModel.currentText(), 
                    self.cmbSize.currentText() )
        self.lblGtin.setText( "Выбран GTIN:%s"%( self.GTIN ) )
        
        marks = dif_func.readNumberOfCodes( DBname, self.GTIN )
        self.lblNumber.setText( "Всего доступно %s кодов."%( marks ) )
        self.spnNumber.setMaximum( marks )
             
    def readModels( self, name ):
        res = dif_func.getAllModels( DBname )
        self.cmbModel.clear()
        self.cmbModel.addItems( sorted( res ) )
        self.readSizes()
        
    def readSizes( self ):
        res = dif_func.readSizesByModel( DBname,  self.cmbModel.currentText() )
        self.cmbSize.clear()
        self.cmbSize.addItems( sorted( res ) )
        self.calculateCodes()
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication( sys.argv )
    window = Print_Codes_Window( 'DB' )
    window.show()
    sys.exit( app.exec_() )
