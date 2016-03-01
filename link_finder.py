#!/usr/bin/python
from HTMLParser import HTMLParser
from urllib import *

class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print(tag)

    def error(self, message):
        pass

finder = LinkFinder()
finder.feed('<html><head><title>test</title></head>'
        '<body><h1>parse me</h1></body></html>')
