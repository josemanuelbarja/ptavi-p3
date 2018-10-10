#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smallsmilhandler
from xml.sax import make_parser

if __name__ == '__main__':
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        print('Usage: python3 karaoke.py fichero.smil')
    lista = cHandler.get_tags()
    for lineas in lista:
        print(lineas['name'], end = '\t')
        for indice, valor in lineas.items():
            if valor != '' and indice != 'name':
                print(indice,'=', """ " """+valor+""" " """, end = '\t')
        print(end = '\n')
    
