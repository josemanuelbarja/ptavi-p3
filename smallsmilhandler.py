#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self): #  'inicializo diccionarios y lista'
        self.root_layout = {'name': 'root_layout'}
        self.region = {'name': 'region'}
        self.image = {'name': 'image'}
        self.audio = {'name': 'audio'}
        self.textstream = {'name': 'textstream'}
        self.lista = []

    def startElement(self, name, attrs):  #  'Guardo atributos y añado a lista ordenada'
        if name == 'root-layout':
            self.root_layout['width'] = attrs.get('width',"")
            self.root_layout['height'] = attrs.get('height',"")
            self.root_layout['background-color'] = attrs.get('background-color',"")
            self.lista.append(self.root_layout)
        elif name == 'region':
            self.region['id'] = attrs.get('id',"")
            self.region['top'] = attrs.get('top',"")
            self.region['bottom'] = attrs.get('bottom',"")
            self.region['left'] = attrs.get('left',"")
            self.region['right'] = attrs.get('right',"")
            self.lista.append(self.region)
        elif name == 'img':
            self.image['src'] = attrs.get('src',"")
            self.image['region'] = attrs.get('region',"")
            self.image['begin'] = attrs.get('begin',"")
            self.image['dur'] = attrs.get('dur',"")
            self.lista.append(self.image)
        elif name == 'audio':
            self.audio['src'] = attrs.get('src',"")
            self.audio['begin'] = attrs.get('begin',"")
            self.audio['dur'] = attrs.get('dur',"")
            self.lista.append(self.audio)
        elif name == 'textstream':
            self.textstream['src'] = attrs.get('src',"")
            self.textstream['region'] = attrs.get('region',"")
            self.lista.append(self.textstream)

    def get_tags(self):  #  'Me devuelve la lista completa'
        return self.lista

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    lista = cHandler.get_tags()
    
