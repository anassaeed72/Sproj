import os
import sys
def cybox(cyboxXmlValue):
	print "In cybox " + cyboxXmlValue

def nestedOperationFunc(nestedOperationXmlFile):
	print "in nestedOperationFunc " + nestedOperationXmlFile

def ifCondition(conditionValue,leftValue,rightValue,actionValue):
	print "In If Condition" + conditionValue + " " + leftValue+ " " + rightValue+ " " +actionValue
	if conditionValue == "==":
			pass	
	elif conditionValue == "<":
		pass
	elif conditionValue == ">":
		pass

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
	condition = xmldoc.getElementsByTagName('condition')
	conditionValue = condition[0].attributes['myvalue'].value
	left = xmldoc.getElementsByTagName('left')
	leftValue = left[0].attributes['myvalue'].value
	right = xmldoc.getElementsByTagName('right')
	rightValue = right[0].attributes['myvalue'].value
	action = xmldoc.getElementsByTagName('action')
	actionValue = action[0].attributes['myvalue'].value
	ifCondition(conditionValue,leftValue,rightValue,actionValue)
	sys.exit(1)

if operationNameValue =="nestedOperations":
	nestedOperation = xmldoc.getElementsByTagName('nestedOperationXml')
	nestedOperationValue = nestedOperation[0].attributes['myvalue'].value
	nestedOperationFunc(nestedOperationValue)
	sys.exit(1)
	

operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value


operationPath = xmldoc.getElementsByTagName('operationPath')
operationPathValue = operationPath[0].attributes['myvalue'].value


commandToExecute = "python " + operationPathValue + "/" + operationNameValue + ".py " + operationInputFilevalue
print "Command : "+operationNameValue
print commandToExecute
# os.system(commandToExecute)

