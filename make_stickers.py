#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image, ImageDraw, ImageFont

from barcode import EAN13
from barcode.writer import ImageWriter

from PyPDF2 import PdfFileReader

import os
import datetime

dm = "dmcode.png"


def generateSticker(model, size, gtin, serial, dmC):
    lim = 1.2
    w = round( dmC.width * lim )
    h = round( dmC.height * lim )
    print( "%s %s %s %s" % ( model, size, gtin, serial ) )
#    os.system( 'zint --height 20 -o ean.png -b 13 -d "%s"'%( gtin[5:17] ) )
    print(gtin)
    print( gtin[5:18] )
    with open( 'ean.png', 'wb' ) as f:
        EAN13( '%s' % (gtin[5:18]), writer = ImageWriter() ).write( f )
    dmCode = dmC
    dmCode = dmCode.resize( (w, h) )
    img = Image.open("./maket.png")
    img.paste( dmCode, box = (600, 70))

    ean = Image.open("./ean.png")
    ean = ean.crop( (60, 1, 500, 150) )
    img.paste( ean, box = (95, 645))

    w = round( len( model ) * 30 / 2 )
    print( w )

    txt = Image.new( "RGBA", img.size, (255, 255, 255, 0) )
    fnt = ImageFont.truetype( "Pillow/Tests/fonts/FreeMonoBold.ttf", 120 )
    fnt1 = ImageFont.truetype( "Pillow/Tests/fonts/FreeMonoBold.ttf", 45 )

    # get a drawing context
    d = ImageDraw.Draw( txt )

    # draw text, half opacity
    d.text( (110 + w, 130), model, font = fnt, fill = (0, 0, 0, 255) )
    # draw text, full opacity
    d.text( (230, 330), size, font = fnt, fill = (0, 0, 0, 255) )

    d.text( (550, 570), gtin, font = fnt1, fill = (0, 0, 0, 255) )
    d.text( (650, 670), serial, font = fnt1, fill = (0, 0, 0, 255) )

    img = Image.alpha_composite( img, txt )

#    draw.font_size = 110
#    draw.text( 320 - w, 240, model )
#    draw.text( 250, 420, size )
#    draw.font_size = 70



#     draw.font_size = 50
#     draw.text( 580, 630, gtin )
#     draw.text( 680, 720, serial )
#
#     draw( img )
    now = datetime.datetime.now()
    name = "./images/m%s_s%s_%s_%s_%s_%s_%s_%s_%s.png" % ( model, size, now.year,
                                                           now.month, now.day, now.hour,
                                                           now.minute, now.second,
                                                           now.microsecond )
    print(name)
    img.save(name)
    dmCode.save("dout.png")
    
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
    with open('num.txt', 'wt') as f:
        f.write('%s'%(i))
    print( i, all[i][3] )
    tmp = convert_from_path('.//flask_tmp.pdf',
                            dpi = 400, first_page = i + 1 , last_page = i + 1)[0]
    tmp = tmp.crop( (420, 15, 800, 395)  )
    tmp.save('tmp_image.png')
    generateSticker( all[i][0], all[i][1], "(01)" + all[i][2] + "(21)",  all[i][3], tmp )
