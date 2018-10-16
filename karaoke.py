#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
import smallsmilhandler
from xml.sax import make_parser

class KaraokeLocal:

    def local(self, lista):
        smiltojson = sys.argv[1].replace('.smil','.json')
        with open(smiltojson, 'w') as fichjson:
            json.dump(lista, fichjson, indent=4)
        for lineas in lista:
            for indice, valor in lineas.items():
                if indice == 'src':
                    if valor.startswith('http:'):
                        loc = valor.split('/')
                        l = str(loc[-1:])
                        urllib.request.urlretrieve(valor, l[2:-2])

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
    karaoke = KaraokeLocal()
    karaoke.local(lista)
