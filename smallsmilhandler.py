#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.root_layout = {'name': 'root_layout'}
        self.region = {}
        self.image = {}
        self.audio = {}
        self.textstream = {}

    def startElement(self, name, attrs):
        if name == 'root-layout':
            self.root_layout['width'] = attrs.get('width',"")
            self.root_layout['height'] = attrs.get('height',"")
            self.root_layout['background-color'] = attrs.get('background-color',"")
        elif name == 'region':
            self.region['id'] = attrs.get('id',"")
            self.region['top'] = attrs.get('top',"")
            self.region['bottom'] = attrs.get('bottom',"")
            self.region['left'] = attrs.get('left',"")
            self.region['right'] = attrs.get('right',"")
        elif name == 'img':
            self.image['src'] = attrs.get('src',"")
            self.image['region'] = attrs.get('region',"")
            self.image['begin'] = attrs.get('begin',"")
            self.image['dur'] = attrs.get('dur',"")
        elif name == 'audio':
            self.audio['src'] = attrs.get('src',"")
            self.audio['begin'] = attrs.get('begin',"")
            self.audio['dur'] = attrs.get('dur',"")
        elif name == 'textstream':
            self.textstream['src'] = attrs.get('src',"")
            self.textstream['region'] = attrs.get('region',"")

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
