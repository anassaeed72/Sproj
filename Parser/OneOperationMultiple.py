import os
import sys
if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()

from xml.dom import minidom
xmldoc = minidom.parse(sys.argv[1])

operationName = xmldoc.getElementsByTagName('operationName')
operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
operationPath = xmldoc.getElementsByTagName('operationPath')

print "Doing Operation"

for index in range(len(operationName)):
	operationNameValue = operationName[index].attributes['myvalue'].value
	operationInputFilevalue = operationInputFile[index].attributes['myvalue'].value
	operationPathValue = operationPath[index].attributes['myvalue'].value
	commandToExecute = "python " + operationPathValue + "/" + operationNameValue + ".py " + operationInputFilevalue
	print commandToExecute
# os.system(commandToExecute)

