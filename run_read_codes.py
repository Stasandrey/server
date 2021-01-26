#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui#, QtCore
import read_codes
import dif_func
DBname = "DB"
class Read_Codes( QtWidgets.QWidget, read_codes.Ui_Read_Codes ):
    def __init__( self, database, parent = None   ):
        QtWidgets.QWidget.__init__( self, parent )
        self.setupUi( self )
        
        self.model = QtGui.QStandardItemModel( parent = self )   
        self.lstInside.setModel( self.model )
#        self.header = QtWidgets.QHeaderView( QtCore.Horizontal )
#        self.treeScan.setHeader( self.header )        
        self.f = False;
        self.korob = '';
        self.inside = []
        self.edtCode.editingFinished.connect( self.analizeCode )
        self.btnClear.clicked.connect( self.btn_clear )
#       self.btnSetup.clicked.connect( self.btn_setup )
        self.btnClose.clicked.connect( self.close )
        
    
    def btn_clear( self ):
        self.edtCode.clear()
   
    def analizeCode( self ):
        res = self.edtCode.text()
        self.edtCode.clear()
        if len( res ) == 18:
            if dif_func.isSsccFree( DBname, res ) == True:
                self.model.clear()
                
                self.lblKorob.setText( "Короб %s."%( res ) )
                self.korob = res
                self.f = True
            else:
                print( "No SSCC" )
        
        
        if len( res ) > 18:
            if self.f ==True:
                res = dif_func.getGtinSerialByCode( res )
                now = []
                if dif_func.isGtinExist( DBname, res[0] ) ==False:
                    s, ok = QtWidgets.QInputDialog.getText( None, 
                                        "Данный GTIN отсутствует в базе.", 
                                        "Введите название модели:")
                    s1, ok1 = QtWidgets.QInputDialog.getText( None, 
                                        "Данный GTIN отсутствует в базе.", 
                                        "Введите размер:")
                    if ok:
                        if ok1:
                            dif_func.addGtin( DBname, res[0], s, s1 )
                sn = res[1]
                res[1] = dif_func.encodeSerial( res[1] )
                if dif_func.isCodeExist( DBname, res[0], res[1] ) == False:
                    dif_func.addCode( DBname, res[0], res[1], "", 1 )
                now.append( res[0] )
                now.append( res[1] )
                now.append( self.korob )
                self.inside.append( now )
                
                print( now )
                print( self.inside )
                s = dif_func.getModelSizeByGtin( DBname, res[0] )
                print( s )
                dif_func.markCodeInKorob( DBname, now )
                item = QtGui.QStandardItem( "GTIN: " + now[0] + "  S/N: " + sn + "  Модель: " + s[0].rjust( 10 ) + "  Размер " + s[1] )
                self.model.appendRow( item )
#                self.lstInside.
            #    self.lblGtin.setText( "GTIN:" + res[0] )
#                self.lblSerial.setText( "Серийный номер:" + res[1] )
#                res = dif_func.getModelSizeByGtin( DBname, res[0] )
#                self.lblModel.setText( "Модель:" + res[0] )
#                self.lblSize.setText( "Размер:" + res[1] )
            
                print( res )
            else:
                print( "No korob" )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication( sys.argv )
    window = Read_Codes( 'DB' )
    window.show()
    sys.exit( app.exec_() )
