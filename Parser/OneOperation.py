import os
import sys
from lxml import etree
import xml.etree.ElementTree
from Constants import ConstantsClass
import subprocess
from pymongo import MongoClient

def cybox(cyboxXmlValue):
	print "In cybox " + cyboxXmlValue

def nestedOperationFunc(nestedOperationXmlFile):
	print "in nestedOperationFunc " + nestedOperationXmlFile
	os.system('python MultipleOperations.py '+nestedOperationXmlFile)


def flatten(seq,fileName):
  count = 0
  for item in seq:
  	if count == 0:
  		count = 1
  		continue
	if isinstance(item,(etree._Element,)):
	    with open(fileName, "w") as myfile:
    		myfile.write(etree.tostring(item,with_tail=False))
    		myfile.close()
    		os.system("python IfConditionMultiple.py IfConditionMultipleXmlTemp.xml 0")
    
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
	sys.exit(0)

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
	sys.exit(0)

if operationNameValue == "ifMultiple":
	e = etree.parse(sys.argv[1])
	flatten(e.xpath('/operation/node()'),"IfConditionMultipleXmlTemp.xml")
	
	sys.exit(0)

if operationNameValue =="nestedOperations":
	nestedOperation = xmldoc.getElementsByTagName('nestedOperationXml')
	nestedOperationValue = nestedOperation[0].attributes['myvalue'].value
	nestedOperationFunc(nestedOperationValue)
	sys.exit(0)

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
	sys.exit(0)

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
	sys.exit(0)
if operationNameValue=="exit":
	exitCommand = "exit"
	print exitCommand
	sys.exit(0)

if operationNameValue=="Bulk_Extractor":
	print "Bulk_Extractor"
	operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
	operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value
	operationInputFilevalue = ConstantsClass.pathValue+operationInputFilevalue

	operationPath = xmldoc.getElementsByTagName('operationPath')
	operationPathValue = operationPath[0].attributes['myvalue'].value
	operationPathValue = ConstantsClass.pathValue + operationPathValue
	command = "bulk_extractor -E net -o "+operationPathValue+" " +operationInputFilevalue
	print command
	os.system(command)
	sys.exit()	

if operationNameValue=="TCP_DUMP":
	print "TCP DUMP"
	operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
	operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value
	operationInputFilevalue = ConstantsClass.pathValue+operationInputFilevalue

	
	command = "sudo tcpdump -tttttnnr "+operationInputFilevalue+" | grep IP"
	print command
	outputTcpDump = subprocess.check_output((command),shell=True)
	for lines in outputTcpDump.split('\n'):
		print "Line "+lines
		count =0
		aDict2={}
		aDict =[]
		for word in lines.split(' '):
			print "word " + word
			if count ==2:
				# insert sender IP here
				aDict2["SenderIP"] = word
			elif count == 4:
				# insert recieve IP here
				aDict2["ReceiverIP"] = word
				break
			count = count+1
		

	aDict.append(aDict2)
	aDict2={}
	client = MongoClient()
	db = client.test
	db.randCollection.insert_many(aDict)
	
	# # db.randCollection.aggregate([{$group: {_id,  "SenderIP": {$sum: "$SenderIP"}}}])
	# pipe = [{'$group': {'_id': None,'SenderIP': {'$sum': '$SenderIP'}}}]
	# db.randCollection.aggregate(pipeline=pipe)
	
	cursor = db.randCollection.find()
	for document in cursor:
		print ' '.join('| {} : {} |'.format(key, val) for key, val in sorted(document.items()))
		
	sys.exit()	

operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value
operationInputFilevalue = ConstantsClass.pathValue+operationInputFilevalue

operationPath = xmldoc.getElementsByTagName('operationPath')
operationPathValue = operationPath[0].attributes['myvalue'].value
operationPathValue = ConstantsClass.pathValue + operationPathValue

commandToExecute = "python " + operationPathValue + "/" + operationNameValue + ".py " + operationInputFilevalue
print "Command : "+operationNameValue
print commandToExecute
os.system(commandToExecute)

