import os
import sys
import subprocess

from lxml import etree
import xml.etree.ElementTree
from Print import Print
from Constants import PrintLevel
from Constants import ConstantsClass
from OneOperation import OneOperation
from xml.dom import minidom

def findFileName(input):
    array = input.split("/")
    return array[len(array)-1]

def printDescription(description):
    Print.Print(PrintLevel.NewLine, "")
    Print.Print(PrintLevel.BaseClass,"Descrition:  " + description)
    Print.Print(PrintLevel.NewLine, "\n")

if len(sys.argv) <2:
    Print.Print(PrintLevel.BaseClass,'Arguments not given')
    sys.exit()


Print.Print(PrintLevel.BaseClass,"In Multiple Operations")
Print.Print(PrintLevel.NewLine, "\n\n\n")
Print.Print(PrintLevel.BaseClass, "Running File  " + findFileName(sys.argv[1]))

xmldoc = minidom.parse(sys.argv[1])
descriptionObject = xmldoc.getElementsByTagName('operations')
try:
    descriptionObjectValue = descriptionObject[0].attributes['description'].value
    printDescription(descriptionObjectValue)
except Exception, e:
    pass


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




