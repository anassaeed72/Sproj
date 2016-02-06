import os
import sys
def cybox(cyboxXmlValue):
	print "In cybox " + cyboxXmlValue

def ifCondition():
	print "In If Condition"
if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()

from xml.dom import minidom
xmldoc = minidom.parse(sys.argv[1])

operationName = xmldoc.getElementsByTagName('operationName')
operationNameValue = operationName[0].attributes['myvalue'].value

if operationNameValue == "cybox":
	cyboxXml = xmldoc.getElementsByTagName('cyboxXml')
	cyboxXmlValue = cyboxXml[0].attributes['myvalue'].value
	cybox(cyboxXmlValue)
	sys.exit(1)

if operationNameValue =="IfCondition":
	ifCondition()
	

operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value


operationPath = xmldoc.getElementsByTagName('operationPath')
operationPathValue = operationPath[0].attributes['myvalue'].value


commandToExecute = "python " + operationPathValue + "/" + operationNameValue + ".py " + operationInputFilevalue
print "Command : "+operationNameValue
print commandToExecute
# os.system(commandToExecute)

