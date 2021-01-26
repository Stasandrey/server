#!/usr/bin/python3
# -*- coding: utf-8 -*-
#*******************************************************************************
#     Функции для генерации и формирования изображения SSCC
#      initialize( name )
#           создает новую базу данных в файле name 
#      generateSSCC( name, prefix )
#           генерирует код с префиксом, которого нет в базе старых кодов name
#     
#
#*******************************************************************************

import sqlite3
import time


def initialize( name ):
    con = sqlite3.connect( name )
    con.execute( "CREATE TABLE SSCC (\
                SSCC TEXT,\
                CONTROL TEXT, \
                STATUS INTEGER,\
                DATE_CREATE TEXT\
                );" )
    con.commit()
    con.close()

def calculateControlDigit( s ):
    i = 16
    chet = 0;
    nechet = 0;
    while i >=0:
        if i%2==0:
            nechet = nechet + int( s[i] )
        else:
            chet = chet + int( s[i] )
        i = i - 1
    summa = chet + 3*nechet
    m = str( summa )
    last = int( m[1] )
    if last == 0:
        res = str( 0 )
    else:
        res = str( 10-last )
    return res

def generateSSCC( name, prefix, n ):    
    result = []
    if n > 0:
        con = sqlite3.connect( name ) 
        cur = con.cursor()
        cur.execute( "SELECT * FROM SSCC WHERE CONTROL=''" );
        free = cur.fetchall()
        count_free = len( free )
        have = count_free - n
        i = 0;
        while i < have:
            print( "Забираем существующий" )
            i = i + 1
        new = n - i
        if new > 0:
            cur.execute( "SELECT MAX(SSCC) FROM SSCC;" )
            res = cur.fetchone()
           
            if res[0] == None:
                next = '0000000'
            else :
                
                next = res[0]
                next = next[10:17]
                next = str( int( next ) + 1 ).zfill( 7 )
            work = prefix + next 
            control = calculateControlDigit( work )
            i = 0
            while i < new:
                cur.execute( "INSERT INTO SSCC ( SSCC, CONTROL, STATUS, DATE_CREATE )\
                      VALUES ( '%s', '%s', 0, '%s' );"\
                                %( work, control, time.strftime( "%d.%m.%Y" ) ) )
                result.append( work + control )
                next = str( int( next ) + 1 ).zfill( 7 )
                work = prefix + next
                control = calculateControlDigit( work )
                i = i + 1
        con.commit()
        con.close()
    return result

if __name__ == "__main__":
    import sys
    if len( sys.argv ) == 2:
        initialize( sys.argv[1] )
        print( "Создана база данных SSCC под именем [%s]."%( sys.argv[1] ) )
    else:
        res = generateSSCC( 'DB', '0464005095', 10 )

