#!/usr/bin/python

import sys
from lxml import etree

file = sys.argv[1]

parser = etree.XMLParser(remove_blank_text=True)

data = etree.parse(file, parser)

namespaces = data.getroot().nsmap

ns = namespaces[None]

contentTag = '//{%s}content' % ns
iconTag = '//{%s}icon' % ns

files = data.find(contentTag).xpath('.//text()')

iconNodes = data.find(iconTag)

if iconNodes is not None:
    files += iconNodes.xpath('.//text()')

print ' '.join(files)
