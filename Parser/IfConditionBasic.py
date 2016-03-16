import os
import sys
from lxml import etree
import xml.etree.ElementTree
import re
from pymongo import MongoClient
from operator import itemgetter
from collections import OrderedDict
from Print import Print
from Constants import PrintLevel
if len(sys.argv) <2:
	Print.Print(PrintLevel.Command,'Arguments not given')
	sys.exit()

from xml.dom import minidom
xmldoc = minidom.parse(sys.argv[1])

left = xmldoc.getElementsByTagName('key')
leftValue = left[0].attributes['myvalue'].value
right = xmldoc.getElementsByTagName('value')
rightValue = right[0].attributes['myvalue'].value

collection = xmldoc.getElementsByTagName('collection')
collectionValue = collection[0].attributes['myvalue'].value

operator = xmldoc.getElementsByTagName('operator')
operatorValue = operator[0].attributes['myvalue'].value

client = MongoClient()
db = client.test

if collectionValue=="DOSCollection":
	cursor = list(db.randCollection.aggregate([
    {"$group" : {"_id" : "$SenderIP", "count":  { "$sum" : 1}}

    }
	]))
	if operatorValue=="average":
		countOfDocuments = 0
		countOfPackets = 0
		for document in cursor:
			countOfDocuments = countOfDocuments +1
			countOfPackets+=document["count"]
		averageValue = countOfPackets/countOfDocuments
		if averageValue > int (rightValue):
			Print.Print(PrintLevel.IfConditionAnswer,"true")
		else:
			Print.Print(PrintLevel.IfConditionAnswer,"false")
		sys.exit()

	if operatorValue=="sum":
		countOfDocuments = 0
		countOfPackets = 0
		for document in cursor:
			countOfPackets+=document["count"]
		if countOfPackets > int (rightValue):
			Print.Print(PrintLevel.IfConditionAnswer,"true")
		else:
			Print.Print(PrintLevel.IfConditionAnswer,"false")
		sys.exit()

	
	for document in cursor:
		# print document
		if document["_id"]== leftValue:
			if document["count"]>=int(rightValue):
				Print.Print(PrintLevel.IfConditionAnswer,"true")
			else:
				Print.Print(PrintLevel.IfConditionAnswer,"false")
			sys.exit()
	Print.Print(PrintLevel.IfConditionAnswer,"false")
	sys.exit()

if operatorValue =="contains":
	key_ =leftValue# sys.argv[2] # key is col and value is 127.0.0.1
	value =rightValue# sys.argv[3]

	key_val = {}
	key_val[key_] = value

	cursor = db[collectionValue].find(key_val)


	if cursor.count() >0:
		Print.Print(PrintLevel.IfConditionAnswer,"true")
	else:
		Print.Print(PrintLevel.IfConditionAnswer,"false")
	sys.exit()
