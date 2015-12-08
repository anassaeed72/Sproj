import os
import sys
from lxml import etree
import xml.etree.ElementTree

if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()

e = etree.parse(sys.argv[1])

def flatten(seq):
  for item in seq:
    if isinstance(item,(etree._Element,)):
    	with open("OneOperationsTempXml.xml", "w") as myfile:
    		myfile.write(etree.tostring(item,with_tail=False))
    		myfile.close()
  	  	os.system('python OneOperation.py OneOperationsTempXml.xml')

flatten(e.xpath('/operations/node()'))

