#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets#, QtGui, QtCore
import main_window
import run_read_datamatrix_stickers
import run_print_codes
import run_read_codes
DBname = "DB"
class Main_Window( QtWidgets.QWidget, main_window.Ui_Main_Window ):
    def __init__( self, database, parent = None   ):
        QtWidgets.QWidget.__init__( self, parent )
        self.setupUi( self )
        
        self.btnOrders.clicked.connect( self.btn_orders )
        self.btnPrintDatamatrix.clicked.connect( self.btn_print_datamatrix )
        self.btnAgregation.clicked.connect( self.btn_agregation )
#        self.btnSetup.clicked.connect( self.btn_setup )
        self.btnClose.clicked.connect( self.close )

    def btn_agregation( self ):
        self.wnd = run_read_codes.Read_Codes( DBname )
        self.wnd.show()

    def btn_print_datamatrix( self ):
        self.wnd = run_print_codes.Print_Codes_Window( DBname )
        self.wnd.show()
    
    def btn_orders( self ):
        self.wnd = run_read_datamatrix_stickers.Read_Datamatrix_Stickers_Window( DBname )
        self.wnd.show()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication( sys.argv )
    window = Main_Window( 'DB' )
    window.show()
    sys.exit( app.exec_() )
