import sys
import os
class OneOperationGenerator:
	operationName = ""
	operationInputFile=""
	operationPath=""
	fileName=""
	def OneOperationGenerator():
		operationName = ""
	
	def writeToFile(self):
		print ("Writing to file")
		if len(self.fileName) == 0:
			print ("Enter File Name")
			sys.exit(1)
		with open(self.fileName,"w") as myfile:
			myfile.write("<operation>\n")	
			myfile.write("	<operationName myvalue=\"" + self.operationName+"\"/>\n")
			myfile.write("		<operationInputFile myvalue=\""+self.operationInputFile+"\"/>\n")
			myfile.write("		<operationPath myvalue=\""+self.OperationPath+"\" />\n")
			myfile.write("</operation>\n")
			myfile.close();


one = OneOperationGenerator()
one.operationName = "test"
one.fileName = "test.xml";
one.operationInputFile = "tempinputfile";
one.OperationPath = "OperationPath"
one.writeToFile()