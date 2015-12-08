import os
import subprocess
import sys
import xml.etree.ElementTree
from xml.dom import minidom
if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()



from xml.dom import minidom
xmldoc = minidom.parse(sys.argv[1])

operationName = xmldoc.getElementsByTagName('operationName')
# print(operationName[0].attributes['myvalue'].value)
operationNameValue = operationName[0].attributes['myvalue'].value


operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
# print(operationInputFile[0].attributes['myvalue'].value)
operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value


operationPath = xmldoc.getElementsByTagName('operationPath')
# print(operationPath[0].attributes['myvalue'].value)
operationPathValue = operationPath[0].attributes['myvalue'].value

print "Doing Operation"


commandToExecute = "python " + operationPathValue + "/" + operationNameValue + ".py " + operationInputFilevalue
os.system(commandToExecute)
