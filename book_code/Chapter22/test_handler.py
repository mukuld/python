from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler): pass
parse('website.xml', TestHandler())

    def startElement(self, name, attrs):
        print name, attrs.keys()
