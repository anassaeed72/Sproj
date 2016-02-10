import os
import sys
def cybox(cyboxXmlValue):
	print "In cybox " + cyboxXmlValue

def nestedOperationFunc(nestedOperationXmlFile):
	print "in nestedOperationFunc " + nestedOperationXmlFile
	os.system('python MultipleOperations.py '+nestedOperationXmlFile)



def ifCondition(conditionValue,left,right,yesactionValue,noactionValue):
	print "In If Condition" + conditionValue + " " + left+ " " + right+ " " +yesactionValue +  " " + noactionValue

	with open(left) as leftFile:
	    	content = leftFile.readline()

	rightValue = right
	if conditionValue == "==":
		if leftValue == rightValue:
			nestedOperationFunc(yesactionValue)	
		else:
			nestedOperationFunc(noactionValue)	
	elif conditionValue == "<":
		if leftValue < rightValue:
			nestedOperationFunc(yesactionValue)	
		else:
			nestedOperationFunc(noactionValue)	
	elif conditionValue == ">":
		if leftValue > rightValue:
			nestedOperationFunc(yesactionValue)	
		else:
			nestedOperationFunc(noactionValue)	

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
	yesaction = xmldoc.getElementsByTagName('yesaction')
	yesactionValue = yesaction[0].attributes['myvalue'].value

	noaction = xmldoc.getElementsByTagName('noaction')
	noactionValue = noaction[0].attributes['myvalue'].value

	ifCondition(conditionValue,leftValue,rightValue,yesactionValue,noactionValue)
	sys.exit(1)

if operationNameValue =="nestedOperations":
	nestedOperation = xmldoc.getElementsByTagName('nestedOperationXml')
	nestedOperationValue = nestedOperation[0].attributes['myvalue'].value
	nestedOperationFunc(nestedOperationValue)
	sys.exit(1)

if operationNameValue =="DOS":
	operationInputFile = xmldoc.getElementsByTagName('operationPath')
	operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value

	vmName = xmldoc.getElementsByTagName('vmName')
	vmNameValue = vmName[0].attributes['myvalue'].value

	minPacket = xmldoc.getElementsByTagName('minPacket')
	minPacketvalue = minPacket[0].attributes['myvalue'].value
	command = "" + operationInputFilevalue +"/DOSOperation.sh " + vmNameValue + " " + minPacketvalue
	print command
	os.system(command)
	sys.exit(1)

if operationNameValue =="getDump":
	operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
	operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value


	operationPath = xmldoc.getElementsByTagName('operationPath')
	operationPathValue = operationPath[0].attributes['myvalue'].value

	vmName = xmldoc.getElementsByTagName('vmName')
	vmNameValue = vmName[0].attributes['myvalue'].value
	command = "python " + operationPathValue +"/getDump.py " + vmNameValue + " " + operationInputFilevalue
	print command
	os.system(command)
	sys.exit(1)
	

operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value


operationPath = xmldoc.getElementsByTagName('operationPath')
operationPathValue = operationPath[0].attributes['myvalue'].value


commandToExecute = "python " + operationPathValue + "/" + operationNameValue + ".py " + operationInputFilevalue
print "Command : "+operationNameValue
print commandToExecute
os.system(commandToExecute)

