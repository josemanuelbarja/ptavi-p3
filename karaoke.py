#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smallsmilhandler
from xml.sax import make_parser

if __name__ == '__main__':
    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    lista = cHandler.get_tags()
    for lineas in lista.items():
        print(lineas)
