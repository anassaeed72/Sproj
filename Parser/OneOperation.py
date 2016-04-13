import os
import sys
from lxml import etree
import xml.etree.ElementTree
from Constants import ConstantsClass
from Print import Print
import subprocess
from pymongo import MongoClient
from Print import Print
from Constants import PrintLevel
from xml.dom import minidom
from IfConditionMultiple import IfConditionMultiple
from time import time
class OneOperation(object):
	"""docstring for OneOperation"""
	def __init__(self, fileName):
		super(OneOperation, self).__init__()
		self.fileName = fileName
		
	def cybox(self, fileNameTemporary):
		Print.Print(PrintLevel.Command,"In cybox "+fileNameTemporary)

	def nestedOperationFunc(nestedOperationXmlFile):
		Print.Print(PrintLevel.Command, "in nestedOperationFunc " + nestedOperationXmlFile)
		os.system('python MultipleOperations.py '+nestedOperationXmlFile)


	def flatten(self,seq,fileName):
	  count = 0
	  for item in seq:
	  	if count == 0:
	  		count = 1
	  		continue
		if isinstance(item,(etree._Element,)):
		    with open(fileName, "w") as myfile:
	    		myfile.write(etree.tostring(item,with_tail=False))
	    		myfile.close()
	    		# os.system("python IfConditionMultiple.py IfConditionMultipleXmlTemp.xml 0")
	    		IfConditionMultipleBasic = IfConditionMultiple("IfConditionMultipleXmlTemp.xml")
	    		IfConditionMultipleBasic.evaluate()
	    
	def ifCondition(conditionValue,left,right,yesactionValue,noactionValue):
		Print.Print(PrintLevel.IfConditionCondition, "In If Condition" + conditionValue + " " + left+ " " + right+ " " +yesactionValue +  " " + noactionValue)

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
	def flattenCybox(self,seq,fileNameTemporary):
		for item in seq:
			if isinstance(item,(etree._Element,)):
				with open(fileNameTemporary, "w") as myfile:
					myfile.write(etree.tostring(item,with_tail=False))
					myfile.close()
	def evaluate(self):

		Print.Print(PrintLevel.Command, "In One Operation")
		xmldoc = minidom.parse(self.fileName)

		operationName = xmldoc.getElementsByTagName('operationName')
		operationNameValue = operationName[0].attributes['myvalue'].value

		if operationNameValue == "cybox":
			e = etree.parse(self.fileName)
			fileNameTemporary = "CyboxOneOperationXmlTemp"+ str(time()) + ".xml"
			self.flattenCybox(e.xpath('/operation/node()'),fileNameTemporary)

			cybox(fileNameTemporary)
			return
		if operationNameValue == "nestedSchema":
			e = etree.parse(self.fileName)
			fileNameTemporary = "MultipleOperationsTempXml"+ str(time()) + ".xml"
			self.flattenCybox(e.xpath('/operation/node()'),fileNameTemporary)
			commandToExecute = "python MultipleOperations.py " + fileNameTemporary
			Print.Print(PrintLevel.Command, "Command  " + operationNameValue)
			Print.Print(PrintLevel.Command,commandToExecute)
			os.system(commandToExecute)	
			return

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
			e = etree.parse(self.fileName)
			self.flatten(e.xpath('/operation/node()'),"IfConditionMultipleXmlTemp.xml")
			
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
			Print.Print(PrintLevel.Command, command)
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
			Print.Print(PrintLevel.Command, command)
			os.system(command)
			sys.exit(0)
		if operationNameValue=="exit":
			exitCommand = "exit"
			Print.Print(PrintLevel.Command, exitCommand)
			return "exit"
			sys.exit(0)

		if operationNameValue=="Bulk_Extractor":
			Print.Print(PrintLevel.Command, "Bulk_Extractor")
			operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
			operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value
			operationInputFilevalue = ConstantsClass.pathValue+operationInputFilevalue

			operationPath = xmldoc.getElementsByTagName('operationPath')
			operationPathValue = operationPath[0].attributes['myvalue'].value
			operationPathValue = ConstantsClass.pathValue + operationPathValue
			command = "bulk_extractor -E net -o "+operationPathValue+" " +operationInputFilevalue
			Print.Print(PrintLevel.Command, command)
			os.system(command)
			sys.exit()	

		if operationNameValue=="TCP_DUMP":
			Print.Print(PrintLevel.Command,"TCP DUMP")
			operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
			operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value
			operationInputFilevalue = ConstantsClass.pathValue+operationInputFilevalue

			
			command = "sudo tcpdump -tttttnnr "+operationInputFilevalue+" | grep IP"
			Print.Print(PrintLevel.Command, command)
			outputTcpDump = subprocess.check_output((command),shell=True)
			aDict =[]
			for lines in outputTcpDump.split('\n'):
				count =0
				aDict2={}
				
				for word in lines.split(' '):
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
			db.DOSCollection.insert_many(aDict)
			sys.exit()
		if operationNameValue =="CustomPython":
			operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
			operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value

			operationPath = xmldoc.getElementsByTagName('operationPath')
			operationPathValue = operationPath[0].attributes['myvalue'].value
			operationPathValue = ConstantsClass.pathValue + operationPathValue +"/"+ operationInputFilevalue
			
			commandToExecute = "python " + operationPathValue
			Print.Print(PrintLevel.Command, "Command  " + operationNameValue)
			Print.Print(PrintLevel.Command,commandToExecute)
			os.system(commandToExecute)			
			#cursor = list(db.randCollection.aggregate([
			 #    {"$group" : {"_id" : "$SenderIP", "count":  { "$sum" : 1}}

		 	#    }
			# ]))
			# for document in cursor:
			# 	print document
			# 	# print ' '.join('| {} : {} |'.format(key, val) for key, val in sorted(document.items()))
			# db.DOSCollection.insert(cursor)
			# db.DOSCollection.remove()
			# cursor = db.DOSCollection.find()
			# print "after cursor is obtained"
			# for document in cursor:
			# 	print "oneline"
			# 	print ' '.join('| {} : {} |'.format(key, val) for key, val in sorted(document.items()))

				
			sys.exit()	
		if operationNameValue == "Alert":
			operationWords = xmldoc.getElementsByTagName('operationWords')
			operationWordsValue = operationWords[0].attributes['myvalue'].value

			operationLevel = xmldoc.getElementsByTagName('operationLevel')
			operationLevelValue = operationLevel[0].attributes['myvalue'].value

			if operationLevelValue  == "Alpha":			
				Print.Print(PrintLevel.Alpha,operationWordsValue)
			elif operationLevelValue == "Beta":
				Print.Print(PrintLevel.Beta,operationWordsValue)
			elif operationLevelValue == "Gamma":
				Print.Print(PrintLevel.Gamma,operationWordsValue)
			return


		operationInputFile = xmldoc.getElementsByTagName('operationInputFile')
		operationInputFilevalue = operationInputFile[0].attributes['myvalue'].value
		operationInputFilevalue = ConstantsClass.pathValue+operationInputFilevalue

		operationPath = xmldoc.getElementsByTagName('operationPath')
		operationPathValue = operationPath[0].attributes['myvalue'].value
		operationPathValue = ConstantsClass.pathValue + operationPathValue

		commandToExecute = "python " + operationPathValue + "/" + operationNameValue + ".py " + operationInputFilevalue
		Print.Print(PrintLevel.Command,"Command : "+operationNameValue)
		# Print.Print(PrintLevel.Command, commandToExecute)
		os.system(commandToExecute)

