#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtPrintSupport, QtGui, QtCore
import print_SSCC
import SSCC_generator
import barcode  
from barcode.writer import ImageWriter

class Print_SSCC_Window( QtWidgets.QWidget, print_SSCC.Ui_Print_SSCC ):
    def __init__( self, database, commonPart, parent = None   ):
        QtWidgets.QWidget.__init__( self, parent )
        self.setupUi( self )
        self.database = database
        self.commonPart = commonPart
        self.printer = QtPrintSupport.QPrinter()
        self.printer.setResolution( 203 )
        self.btnPrint.clicked.connect( self.btn_print )
        self.btnSetup.clicked.connect( self.btn_setup )
        self.btnClose.clicked.connect( self.close )

    def btn_print( self ):
        if self.spnNumber.value() > 0:
            self.lblWork.setText( "Генерация кодов SSCC" )
            codes = SSCC_generator.generateSSCC( self.database, 
                                                                    self.commonPart, 
                                                                    self.spnNumber.value() )
            self.lblWork.setText( "Генерация изображений и печать." )
            self.prgBar.setMaximum( self.spnNumber.value() )
            i = 0;
            painter = QtGui.QPainter()
            painter.begin( self.printer )
            all = self.spnNumber.value()
            for code in codes:
                with open('temp.png', 'wb') as f:
                    barcode.Code128( code, writer=ImageWriter()).write(f)
                    i = i + 1
                    self.prgBar.setValue( i )
                    pixmap = QtGui.QPixmap( "temp.png" )
                    pixmap = pixmap.scaled( self.printer.width(), 
                                        self.printer.height(), 
                                        aspectRatioMode = QtCore.Qt.KeepAspectRatio )
                    painter.drawPixmap( 0, 0, pixmap )
                    if i < all:
                        self.printer.newPage()
            painter.end()
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication( sys.argv )
    window = Print_SSCC_Window( 'DB',  '0464005095' )
    window.show()
    sys.exit( app.exec_() )
