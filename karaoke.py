#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
import smallsmilhandler
from xml.sax import make_parser


class KaraokeLocal:

    def __init__(self, file):

        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file))
        self.lista = cHandler.get_tags()

    def __str__(self):

        pal_str = ''
        for lineas in self.lista:
            pal_str += lineas['name']
            for indice, valor in lineas.items():
                if valor != '' and indice != 'name':
                    pal_str += '\t' + indice + '=' + """ " """+valor+""" " """
            pal_str += '\n'
        return pal_str

    def to_json(self, file):

        smiltojson = sys.argv[1].replace('.smil', '.json')
        with open(smiltojson, 'w') as fichjson:
            json.dump(self.lista, fichjson, indent=4)

    def do_local(self):

        for lineas in self.lista:
            for indice, valor in lineas.items():
                if indice == 'src':
                    if valor.startswith('http:'):
                        loc = valor.split('/')[-1]
                        urllib.request.urlretrieve(valor, loc)
                        lineas['src'] = lineas['src'].replace(valor, loc)

if __name__ == '__main__':

    try:
        file = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python3 karaoke.py fichero.smil')
    karaoke = KaraokeLocal(file)
    print(karaoke)
    karaoke.to_json(file)
    karaoke.do_local()
    karaoke.to_json(file)
    print(karaoke)
