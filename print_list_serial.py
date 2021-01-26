#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dif_func
import sqlite3

name = 'DB'

def readCodes( name ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "SELECT GTIN, SERIAL FROM CODES;" )
    res = cur.fetchall()
    con.commit()
    con.close()
    return res
    
def readGtin( name ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "SELECT GTIN, MODEL, SIZE FROM GTIN;" )
    res = cur.fetchall()
    con.commit()
    con.close()
    gt = {}
    for item in res:
        rec = []
        rec.append( item[1] )
        rec.append( item[2] )
        gt[ item[0] ] = rec;
    
    return gt


gtin = readGtin( name )    

codes = readCodes( name )
for item in codes:
    
    print( "%s %s %s (01)%s(21)%s"%( gtin[ item[0] ][0], gtin[ item[0] ][1], item[0], item[0], dif_func.decodeSerial( item[1] ))  )
