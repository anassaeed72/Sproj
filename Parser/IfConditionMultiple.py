import os
import sys
import subprocess
from lxml import etree
import xml.etree.ElementTree
from Print import Print
from Constants import PrintLevel
from xml.dom import minidom
from IfConditionBasic import IfConditionBasic
class IfConditionMultiple(object):
	"""docstring for IfConditionMultiple"""
	def __init__(self, fileName):
		super(IfConditionMultiple, self).__init__()
		self.fileName = fileName
		self.ifMultipleOperator = "and"
	def flatten(self,seq):
		for item in seq:
			if isinstance(item,(etree._Element,)):
					# if item.tag == "ifConditionMultiple":
					# 	with open("IfConditionMultipleXmlTemp.xml", "w") as myfile:
					# 		myfile.write(etree.tostring(item,with_tail=False))
					# 		myfile.close()
					# 		outputIfBasic = ""
					# 		outputIfBasic = subprocess.check_output(('python IfConditionMultiple.py IfConditionMultipleXmlTemp.xml ' +str(depthCheck)),shell=True)
			  # 	  			if ifMultipleOperator == "or" and outputIfBasic == "true":
			  # 	  				print "true"
			  # 	  				sys.exit() 
			  # 	  			if ifMultipleOperator == "and" and outputIfBasic == "false":
			  # 	  				print "false"
			  # 	  				sys.exit()
					# else:
				with open("IfConditionBasicXmlTemp.xml", "w") as myfile:
					myfile.write(etree.tostring(item,with_tail=False))
					myfile.close()
					outputIfBasic = ""
					outputIfBasic = subprocess.check_output(('python IfConditionBasic.py IfConditionBasicXmlTemp.xml'),shell=True)
					IfConditionBasicObject = IfConditionBasic('IfConditionBasicXmlTemp.xml')
					outputIfBasic = IfConditionBasicObject.evaluate()
					Print.Print(PrintLevel.IfConditionAnswerMultiple, "Basic If Condition Output "+str(outputIfBasic))
		  	  		if self.ifMultipleOperator == "or" and outputIfBasic ==True:
		  	  			Print.Print(PrintLevel.NewLine,"")
		  	  			Print.Print(PrintLevel.IfConditionAnswerMultiple, "If Condition Multiple: True")
		  	  			sys.exit()
		  	  		if self.ifMultipleOperator == "and" and outputIfBasic == False:
		  	  			Print.Print(PrintLevel.NewLine,"")
		  	  			Print.Print(PrintLevel.IfConditionAnswerMultiple,"If Condition Multiple: False")
		  	  			sys.exit()
	def evaluate(self):
		e = etree.parse(self.fileName)
		Print.Print(PrintLevel.BaseClass, "In Multiple If Condition")		
		xmldoc = minidom.parse(self.fileName)
		ifMultiple = xmldoc.getElementsByTagName('ifConditionMultiple')
		self.ifMultipleOperator = "and"#ifMultiple[0].attributes['myvalue'].value
		depthCheck = int(0)
		if depthCheck >10:
			sys.exit()
		depthCheck = depthCheck+1
		

		self.flatten(e.xpath('/ifConditionMultiple/node()'))
		if self.ifMultipleOperator == "and":
			Print.Print(PrintLevel.NewLine,"")
			Print.Print(PrintLevel.IfConditionAnswerMultiple, "If Condition Multiple Final : True")

