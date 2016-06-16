import os
import sys
from lxml import etree
import xml.etree.ElementTree

def flatten(seq):
  for item in seq:
    if isinstance(item,(etree._Element,)):
    	with open("MultipleOperationsTempXml.xml", "w") as myfile:
    		myfile.write(etree.tostring(item,with_tail=False))
    		myfile.close()
  	  	os.system('python MultipleOperations.py MultipleOperationsTempXml.xml')


if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()

from xml.dom import minidom
xmldoc = minidom.parse(sys.argv[1])

loopIterations = xmldoc.getElementsByTagName('loop')
loopIterationsValue = loopIterations[0].attributes['myvalue'].value
e = etree.parse(sys.argv[1])

for index in range(int(loopIterationsValue)):
	flatten(e.xpath('/loop/node()'))
