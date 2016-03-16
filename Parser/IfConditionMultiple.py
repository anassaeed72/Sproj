import os
import sys
import subprocess
from lxml import etree
import xml.etree.ElementTree
from Print import Print
from Constants import PrintLevel
from xml.dom import minidom
class IfConditionMultiple(object):
	"""docstring for IfConditionMultiple"""
	def __init__(self, fileName):
		super(IfConditionMultiple, self).__init__()
		self.fileName = fileName
	def evaluate():
		e = etree.parse(fileName)
		Print.Print(PrintLevel.BaseClass, "In Multiple If Condition")		
		xmldoc = minidom.parse(sys.argv[1])
		ifMultiple = xmldoc.getElementsByTagName('ifConditionMultiple')
		ifMultipleOperator = "and"#ifMultiple[0].attributes['myvalue'].value
		depthCheck = int(sys.argv[2])
		if depthCheck >10:
			sys.exit()
		depthCheck = depthCheck+1
		def flatten(seq):
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
						Print.Print(PrintLevel.IfConditionAnswer, "Basic If Condition Output "+outputIfBasic)
			  	  		if ifMultipleOperator == "or" and outputIfBasic ==True:
			  	  			Print.Print(PrintLevel.IfConditionAnswer, "true If Condition Multiple")
			  	  			sys.exit()
			  	  		if ifMultipleOperator == "and" and outputIfBasic == False:
			  	  			Print.Print(PrintLevel.IfConditionAnswer,"false If Condition Multiple")
			  	  			sys.exit()

		flatten(e.xpath('/ifConditionMultiple/node()'))
		if ifMultipleOperator == "and":
			Print.Print(PrintLevel.IfConditionAnswer, "true If Condition Multiple Final")
