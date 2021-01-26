#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets#, QtGui, QtCore
import read_datamatrix_stickers
from wand.drawing import Drawing
from wand.image import Image
import sqlite3
import os
import time
import dif_func
from PyPDF2 import PdfFileReader
import datetime
DBname = 'DB'

class Read_Datamatrix_Stickers_Window( QtWidgets.QWidget, 
                                            read_datamatrix_stickers.Ui_Read_Datamatrix_Stickers ):
    def __init__( self, database, parent = None   ):
        QtWidgets.QWidget.__init__( self, parent )
        self.setupUi( self )
        self.btnOpen.clicked.connect( self.open )
        self.btnWork.clicked.connect( self.work )
        self.btnClose.clicked.connect( self.close )

    def open( self ):
        dlg = QtWidgets.QFileDialog( filter = "Файлы заказов (*.pdf)" )
        dlg.setFileMode( QtWidgets.QFileDialog.ExistingFiles )
        dlg.exec()
        files = dlg.selectedFiles()  
        s = ''
        for name in files:
            s = s + name+';'
        s = s[0:len( s ) - 1]
        self.edtFiles.setText( s )

    def work( self ):
        files = self.edtFiles.text().split( ';' )
        self.prgAll.setMaximum( len( files ) )
        self.prgAll.setValue( 0 )
        print( files )
        i = 0
        for file in files:
            i = i + 1 
            self.read_pdf_text( file )
            self.prgAll.setValue( i )
     
    def isGtinUnable( self,  cur, gtin,  model, razm ):
        
        cur.execute( "SELECT * FROM GTIN WHERE GTIN = '%s' AND\
                    MODEL = '%s' AND \
                    SIZE = '%s';"%( gtin, model, razm ) );
        res = cur.fetchone()

        if res == None:
            res = QtWidgets.QMessageBox.question( None, "Неизвестный GTIN", 
        "GTIN %s отсутствует в базе данных.\nВы хотите добавить его?"%( gtin ))
            if res == QtWidgets.QMessageBox.Yes:
                cur.execute( "INSERT INTO GTIN ( GTIN, MODEL, SIZE )\
                VALUES('%s', '%s', '%s');"%( gtin,  model, razm ) )
        
    
    def read_pdf_text( self, name ):
        pdf = PdfFileReader( name )

        num = pdf.getNumPages()  
               
        print( name )
        os.system( 'pdf2txt "%s" > ./tmp_pdf.txt'%( name ) )
        with open( "tmp_pdf.txt", "rt" ) as f:
            res = f.readlines()
        data = []
        print( res )
        for item in res:
            if item != "\n":
                if item[0:2] != "tm":
                    if item[0:4] != "(01)":
                        
                        if item != "":
                            now = item.lstrip()
                            if now != "":
                                if now[0:2] == "р.":
                                    data.append( now[3:5] )
                                elif now[0] == chr( 0xc ):
                                    data.append( now[1:len( now ) - 1] )
                                elif now[0:2] == "1)":
                                    data.append( now[2:len( now ) - 1] )
                                else:
                                    data.append( now[0:len(now) - 1] )
        print( data )
        
        
        i= 0
        all = []
        while i < num:
            item = []
            for j in range( 4 ):
                item.append( data[i*4+j] )
            all.append( item )
            i = i+1
        print( all )
        number = len( all )
        print( number )
        
        print( "Количество кодов->%s"%( number ) )
        self.lblFile.setText( "Преобразование файла %s:"%( name ) )
        con = sqlite3.connect( DBname ) 
        
        cur = con.cursor()

        for i in range( num ):
            print( i )
            tmp = Image( filename = "./1.pdf[%s]"%( i ), resolution = 300 )
            tmp.convert( 'png' ) 
            tmp.crop( 310, 10, 630, 290  )
            self.generateSticker( all[i][0], all[i][1], "(01)" + all[i][2] + "(21)",  all[i][3], tmp, cur )
 

        con.commit()
        con.close()
        self.close()       


    def generateSticker( self, model, size, gtin, serial, dmC, cur ):
        lim = 1.7
        w = round( dmC.width * lim )
        h = round( dmC.height * lim )
        print( "%s %s %s %s"%( model, size, gtin, serial ) )
        dmCode = dmC.clone()
        dmCode.sample( w, h )
        img = Image( filename = "./maket.png" ).clone()
        draw = Drawing()
        draw.composite( operator = "over", left = 600, top = 70, width = dmCode.width,  height = dmCode.height, image = dmCode )
        
        w = round( len( model ) * 65 / 2 ) 
        
        print( w )
        draw.font_size = 110
        draw.text( 320 - w, 240, model )
        draw.text( 250, 420, size )
        draw.font_size = 70
        draw.text( 50, 750, gtin[4 : 18] )
        draw.font_size = 50
        draw.text( 580, 630, gtin )
        draw.text( 680, 720, serial )
       
        draw( img )
    #    now = datetime.datetime.now()
    #    name = "./images/m%s_s%s_%s_%s_%s_%s_%s_%s.png"%( model, size,  now.year,  now.month,  now.day, now.hour, now.minute, now.second )
        fn = dif_func.generateFileName( gtin[ 4: 18 ],  serial )
        img.save( filename = "./images/%s.png"%( fn )  )
        dmCode.save( filename = "dout.png" )
        self.isGtinUnable( cur, gtin[ 4:18 ],  model,  size )
        self.writeToDatabase( cur, gtin[ 4:18 ], serial, fn )
        


#        
#        with open( "tmp_pdf.txt",  "rt" ) as f:
#            res = f.readlines()
#        model = res[1] [ res[1].find(" ") + 1 : len( res[1] ) - 1 ]
#        razm = res[4][ 0 : len( res[4] ) - 1 ]
#        self.isGtinUnable( gtin,  model,  razm )
#        print( res )
#        self.lblFile.setText( "Модель %s, размер %s. Чтение серийных номеров:"%( model, razm) )
#        self.prgFile.setMaximum( len( res ) )
#        self.prgFile.setValue( 0 )
#        i = 0
#        pull = []
#        now = []
#        s = ''
#        flag = 0
#        print( gtin )
#        while i < len( res ):
#            if flag == 1:
#                s = s + res[i][ 0 : len( res[i] ) - 1 ]
#                now = []
#                now.append( gtin )
#                now.append( s[ 18 : len( s ) ] )
#                now.append(dif_func.generateFileName( now[0],  now[1] ) )
#                pull.append( now )
#                flag = 0
#            if flag == 2:
#                flag = 1
#            if res[i].find( "01046" ) != (-1):
#                s = res[i][ 0 : len( res[i] ) - 1 ] 
#                flag = 2
#            i = i + 1
#            self.prgFile.setValue( i )
#        print( pull )
#        self.lblFile.setText( "Получение изображений этикеток" )
#        self.prgFile.setValue( 0 )
#        self.prgFile.setMaximum( int( number ) )
#        i = 0
#        while i < int( number ):
#            print( len( pull ) )
#            print( pull[i] )
#            self.readImage( name,  i,  'images\%s'%( pull[i][2] ) )
#            i = i+1
#            self.prgFile.setValue( i )
#        
#        self.prgFile.setValue( 0 )
#        self.lblFile.setText( "Запись в базу данных." )
#        i = 0
#        con = sqlite3.connect( DBname ) 
#        cur = con.cursor()
#        print( pull )
#        for now in pull:
#            self.writeToDatabase( cur, now[0],  now[1], now[2] )
#            i = i+1
#            self.prgFile.setValue( i )
#        con.commit()
#        con.close()
#        self.close()
    
    def writeToDatabase( self, cur, gtin, serial, fname ):
        d = time.strftime( "%d.%m.%Y" )
        sn = dif_func.encodeSerial( serial )
        cur.execute( "SELECT * FROM CODES WHERE GTIN='%s' AND SERIAL='%s';"%( gtin, sn ) )
        if cur.fetchone() != None:
            print( "Серийный номер %s уже есть в базе."%( serial ) )
        else:
            cur.execute( "INSERT INTO CODES (GTIN, SERIAL,FNAME,DATE,STATUS,GRP)\
       VALUES ( '%s', '%s', '%s', '%s', %s, '%s'); "%( 
                    gtin, sn, fname, d, '0', '' ) );
 
    def readImage( self, name, i,  filename ):
        koord = [ [ 0, 415], 
                        [ 420, 835], 
                        [ 840, 1255], 
                        [ 1260, 1675], 
                        [ 1680, 2095], 
                        [ 2105, 2520],  
                        [ 2525, 2940 ], 
                        [ 2945, 3360 ]  ]
        page = int( i / 8 )
        n = i % 8
        print( "Page %s"%( page ) )
        print( "Image %s"%( n ) )
        with  Image( filename = '%s[%s]'%(  name, page ), resolution = 300 ) as img:
            img.convert( 'png' ) 
            img.crop( 0, koord[n][0], 709, koord[n][1]  )
            img.save( filename = '%s.png'%( filename ) )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication( sys.argv )
    window = Read_Datamatrix_Stickers_Window( 'DB' )
    window.show()
    sys.exit( app.exec_() )
