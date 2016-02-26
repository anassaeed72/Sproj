import os
import sys
from lxml import etree
import xml.etree.ElementTree
import re
from pymongo import MongoClient

if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()

from xml.dom import minidom
xmldoc = minidom.parse(sys.argv[1])

left = xmldoc.getElementsByTagName('key')
leftValue = left[0].attributes['myvalue'].value
right = xmldoc.getElementsByTagName('value')
rightValue = right[0].attributes['myvalue'].value

collection = xmldoc.getElementsByTagName('collection')
collectionValue = collection[0].attributes['myvalue'].value

client = MongoClient()
db = client.test


key_ =leftValue# sys.argv[2] # key is col and value is 127.0.0.1
value =rightValue# sys.argv[3]

key_val = {}
key_val[key_] = value

cursor = db[collectionValue].find(key_val)





if cursor.count() >0:
	print "true"
else:
	print "false"
sys.exit()
# for document in cursor:
	# print ' '.join('| {} : {} |'.format(key, val) for key, val in sorted(document.items()))
# print "If Condition basic"
# print "true"