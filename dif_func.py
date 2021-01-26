#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import sqlite3

def addCode( name, gtin, serial, fname, status ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "INSERT INTO CODES (GTIN, SERIAL, FNAME, DATE,STATUS,GRP) VALUES ('%s','%s','%s','%s',%s,'%s');"%
                            ( gtin, serial, fname, time.strftime( "%d.%m.%Y" ), status, '' ) )
    con.commit()
    con.close()

    

def isCodeExist( name,  gtin, serial ):
    res = False
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "SELECT * FROM CODES WHERE GTIN='%s' AND SERIAL='%s';"%(
                            gtin, serial ) )
    if cur.fetchone() != None:
        res = True
    con.commit()
    con.close()
    return res
    
def addGtin( name, gtin, model, size ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "INSERT INTO GTIN (GTIN, MODEL, SIZE) VALUES ('%s','%s','%s');"%(
                            gtin, model, size ) )
    con.commit()
    con.close()

def isGtinExist( name, gtin ):
    res = False
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "SELECT DISTINCT GTIN FROM GTIN WHERE GTIN='%s';"%(
                            gtin ) )
    if cur.fetchone() != None:
        res = True
    con.commit()
    con.close()
    return res

def isSsccFree( name, sscc ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    s1 = sscc[ 0:  17 ]
    s2 = sscc[17]
    print( s1 )
    print( s2 )
    cur.execute( "SELECT * FROM SSCC WHERE SSCC='%s' AND CONTROL='%s';"%(
                            s1, s2 ) )
    res = cur.fetchone()
    f = False
    print( res )
    if res != None:
        if res[2] == 0:
            f = True
    con.commit()
    con.close()
   
    return f

def getGtinSerialByCode( scan ):
    print( scan )
    res = []
    res.append( scan[ 2 : 16] )
    res.append( scan[ 18 : 31 ] )
    return res

def getModelSizeByGtin( name, gtin ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "SELECT DISTINCT MODEL, SIZE FROM GTIN WHERE GTIN='%s';"%(
                            gtin ) )
    res = cur.fetchone()
    con.commit()
    con.close()
    return res

# Генерирует имя файла на основании GTIN и серийного номера
def generateFileName( gtin, serial ):
    res = ''
    for c in serial:
        res = res + str( ord( c ) )
    res = gtin + res
    return res
        
def encodeSerial( serial ): 
    res = ''
    for c in serial:
        res = res + str( ord( c ) ).zfill( 3 )
    print( res )
    return res
    
def decodeSerial( serial ):
    res = ''
    n = int( len( serial ) / 3 )
    i = 0
    while i < n:
        res = res + chr( int( serial[ i * 3 : i * 3 + 3 ] ) )    
        i = i + 1
    return res
def getAllModels( name ):
        con = sqlite3.connect( name ) 
        cur = con.cursor()
        cur.execute( "SELECT DISTINCT MODEL FROM GTIN;" )
        res = []
        for item in cur.fetchall():
            res.append( item[0] )
#        print( res )
        con.commit()
        con.close()
        return res

def readSizesByModel( name, model ):
        con = sqlite3.connect( name ) 
        cur = con.cursor()
        
        cur.execute( "SELECT DISTINCT SIZE FROM GTIN WHERE MODEL='%s' ;"%( model ) )
#        print( cur.fetchall() )
        res = []
        for item in cur.fetchall():
            res.append( item[0] )
        print( res )
        con.commit()
        con.close()
        return res

def readGtinByModelSize( name,  model, size ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
        
    cur.execute( "SELECT DISTINCT GTIN FROM GTIN\
                WHERE MODEL='%s' AND SIZE='%s';"%
                            ( model,  size ) )
    res = cur.fetchone()[0] 
    con.commit()
    con.close()
    return res

def readNumberOfCodes( name, gtin ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "SELECT * FROM CODES\
                WHERE GTIN='%s' AND STATUS=0 AND GRP='';"%
                            ( gtin ) )
    res = len( cur.fetchall() )
    
    con.commit()
    con.close()
    return res

def readCodesByGtin( name, gtin ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "SELECT GTIN, SERIAL, FNAME FROM CODES\
                WHERE GTIN='%s' AND STATUS=0 AND GRP='';"%( gtin ) )
    res = cur.fetchall()
    con.commit()
    con.close()
    return res
    
def markCodesPrinted( name, printed ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    for item in printed:
        cur.execute( "UPDATE CODES SET STATUS=1 WHERE \
        GTIN='%s' AND SERIAL='%s' AND FNAME='%s';"%
                ( item[0], item[1], item[2] ) )
    con.commit()
    con.close()
 
def markCodeInKorob( name, elem ):
    con = sqlite3.connect( name ) 
    cur = con.cursor()
    cur.execute( "UPDATE CODES SET STATUS=2 WHERE \
        GTIN='%s' AND SERIAL='%s' AND GRP='';"%
                ( elem[0], elem[1] ) )
    cur.execute( "UPDATE CODES SET GRP='%s' WHERE \
        GTIN='%s' AND SERIAL='%s' AND GRP='';"%
                ( elem[2], elem[0], elem[1] ) )
    
    con.commit()
    con.close()

 
if  __name__== "__main__":
    q = input()
    res = encodeSerial( q )
    print( res )
    q = decodeSerial( res )
    print( q )
    
    
