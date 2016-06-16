import os
import sys
import subprocess
from lxml import etree
import xml.etree.ElementTree

if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()
e = etree.parse(sys.argv[1])

def flatten(seq):
	for item in seq:
		if isinstance(item,(etree._Element,)):
			with open("IfConditionBasicXmlTemp.xml", "w") as myfile:
				myfile.write(etree.tostring(item,with_tail=False))
				myfile.close()
  	  			out = subprocess.check_output(('python IfConditionBasic.py IfConditionBasicXmlTemp.xml'),shell=True)
  	  			print "output is "+out

flatten(e.xpath('/ifConditionMultiple/node()'))
