import os
import sys
import subprocess
from lxml import etree
import xml.etree.ElementTree

if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()
e = etree.parse(sys.argv[1])
print "In Multiple If Condition"
from xml.dom import minidom
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
	  	  		if ifMultipleOperator == "or" and outputIfBasic == "true":
	  	  			print "true"
	  	  			sys.exit()
	  	  		if ifMultipleOperator == "and" and outputIfBasic == "false":
	  	  			print "false"
	  	  			sys.exit()

flatten(e.xpath('/ifConditionMultiple/node()'))
if ifMultipleOperator == "and":
	print "true"
