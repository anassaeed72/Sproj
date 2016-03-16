import os
import sys
import subprocess

from lxml import etree
import xml.etree.ElementTree
from Print import Print
from Constants import PrintLevel
from Constants import ConstantsClass
from OneOperation import OneOperation
if len(sys.argv) <2:
	Print.Print(PrintLevel.BaseClass,'Arguments not given')
	sys.exit()
Print.Print(PrintLevel.BaseClass,"In Multiple Operations")
e = etree.parse(sys.argv[1])
outputOneOperation = ""
sys.path.insert(0, ConstantsClass.pathValue+ 'Parser')
def flatten(seq):
  for item in seq:
    if isinstance(item,(etree._Element,)):
    	with open("OneOperationsTempXml.xml", "w") as myfile:
    		myfile.write(etree.tostring(item,with_tail=False))
    		myfile.close()
        OneOperationObject = OneOperation("OneOperationsTempXml.xml")
        OneOperationResult = OneOperationObject.evaluate()
        if OneOperationResult == "exit":
        	sys.exit(0)


flatten(e.xpath('/operations/node()'))

