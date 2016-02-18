import os
import sys
from lxml import etree
import xml.etree.ElementTree
import re
if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()

from xml.dom import minidom
xmldoc = minidom.parse(sys.argv[1])

left = xmldoc.getElementsByTagName('left')
leftValue = left[0].attributes['myvalue'].value
right = xmldoc.getElementsByTagName('right')
rightValue = right[0].attributes['myvalue'].value
operator = xmldoc.getElementsByTagName('operator')
operatorValue = operator[0].attributes['myvalue'].value

print leftValue
print rightValue
print operatorValue
if operatorValue == "equals":
	if leftValue == rightValue:
		print "trueequals"
	else:
		print "false"
elif operatorValue == "greater":
	if leftValue > rightValue:
		print "truegreater"
	else:
		print "false"
elif operatorValue == "smaller":
	if leftValue < rightValue:
		print "truesmaller"
	else:
		print "false"
elif operatorValue =="contains":
	with open(rightValue) as fileObject:
		while True:
			line = fileObject.readLine()
			if not line:
				break
			regex = '*'+leftValue
			matchObj = re.match(regex,line)
			if matchObj:
				print "true1"
				break

	print "false"

