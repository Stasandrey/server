#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

os.system( "pyuic5 print_SSCC.ui -o print_SSCC.py" )
os.system( "pyuic5 read_datamatrix_stickers.ui -o read_datamatrix_stickers.py" )
os.system( "pyuic5 print_codes.ui -o print_codes.py" )
os.system( "pyuic5 read_codes.ui -o read_codes.py" )
os.system( "pyuic5 read_zakaz.ui -o read_zakaz.py" )

os.system( "pyuic5 main_window.ui -o main_window.py" )
