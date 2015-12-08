import os
import sys
if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()

from xml.dom import minidom
xmldoc = minidom.parse(sys.argv[1])

operationName = xmldoc.getElementsByTagName('operationName')
operationNameValue = operationName[0].attributes['myvalue'].value


operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value


operationPath = xmldoc.getElementsByTagName('operationPath')
operationPathValue = operationPath[0].attributes['myvalue'].value


commandToExecute = "python " + operationPathValue + "/" + operationNameValue + ".py " + operationInputFilevalue
print "Command : "+operationNameValue
os.system(commandToExecute)
