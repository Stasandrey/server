#!/usr/bin/python3
# -*- coding: utf-8 -*-

from wand.drawing import Drawing
from wand.image import Image

from barcode import EAN13
from barcode.writer import ImageWriter

from PyPDF2 import PdfFileReader

import os
import datetime

dm = "dmcode.png"


def generateSticker(model, size, gtin, serial, dmC):
    lim = 1.7
    w = round( dmC.width * lim )
    h = round( dmC.height * lim )
    print( "%s %s %s %s" % ( model, size, gtin, serial ) )
#    os.system( 'zint --height 20 -o ean.png -b 13 -d "%s"'%( gtin[5:17] ) )
    print(gtin)
    print( gtin[5:18] )
    with open( 'ean.png', 'wb' ) as f:
        EAN13( '%s' % (gtin[5:18]), writer = ImageWriter() ).write( f )
    dmCode = dmC.clone()
    dmCode.sample( w, h )
    img = Image( filename = "./maket.png" ).clone()
    draw = Drawing()
    draw.composite( operator = "over", left = 600, top = 70, width = dmCode.width,
                    height = dmCode.height, image = dmCode )
    
    w = round( len( model ) * 65 / 2 ) 
    
    print( w )
    draw.font_size = 110
    draw.text( 320 - w, 240, model )
    draw.text( 250, 420, size )
    draw.font_size = 70
    
    ean = Image( filename = "./ean.png", resolution = 300 ).clone()
    draw.composite( operator = "over", left = 24, top = 638,
                    width = round( ean.width * 1  ), height = round( ean.height * 0.65  ),
                    image = ean )
#    draw.text( 50, 750, gtin[4 : 18] )
    draw.font_size = 50
    draw.text( 580, 630, gtin )
    draw.text( 680, 720, serial )
   
    draw( img )
    now = datetime.datetime.now()
    name = "./images/m%s_s%s_%s_%s_%s_%s_%s_%s.png" % ( model, size, now.year,
                                                        now.month, now.day, now.hour,
                                                        now.minute, now.second )
    img.save( filename = name )
    dmCode.save( filename = "dout.png" )
    
# Reading text information
# num = int( input( "Количество->" ) )

# Подсчет количества страниц в PDF файле


name = "./flask_tmp.pdf"
with open(name, 'rb') as f:
    pdf = PdfFileReader(name)
    num = pdf.getNumPages()

print( num )

os.system( 'pdftotext -enc UTF-8 -eol dos %s tmp_pdf.txt' % ( name ) )
# os.system( 'pdf2txt %s > tmp_pdf.txt'%( name ) )
with open( "tmp_pdf.txt", "rt" ) as f_in:
    res = f_in.readlines()
data = []
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


i = 0
all = []
while i < num:
    item = []
    for j in range( 4 ):
        item.append( data[i*4+j] )
    all.append( item )
    i = i+1
print( all )
"""for line in res:
    if line != "\n":
        if line != "0\n":
            if line != "\x0c":
                data.append( line.rstrip() )
print( data )
model = data[0][0 : data[0].find( '(' ) - 1]
size = data[0][data[0].find( '(' ) + 1 : data[0].find( ')' )]
gtin = data[1]
serial = data[2]
"""
# Reading datamatrix code
for i in range( num ):
    print( i )
    tmp = Image( filename = "./flask_tmp.pdf[%s]" % ( i ), resolution = 300 )
    tmp.convert( 'png' ) 
    tmp.crop( 310, 10, 630, 290  )
    generateSticker( all[i][0], all[i][1], "(01)" + all[i][2] + "(21)",  all[i][3], tmp )
