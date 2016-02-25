from pymongo import MongoClient
import json
import sys
import os
import subprocess
import sys

print  "Connscan Zeeshan"
commandToExecute = 'python vol.py -f ' + sys.argv[1] + " connscan"
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
f=proc.communicate()[0]

print "Connscan done"
count = 0
aDict = []
aDict2= {}
for line in f.split("\n"):
	count = count +1
	if count == 1:
		line2 = line
		line2 = line2.strip()
		line2 = line2.split("\n")
		line2 = line2[0].split()
	else:
		if count > 2:
			line = line.strip()

			parts = line.split("\t")
			parts = parts[0].split()
			count2 = 0
			for word in parts:
				if count2 < (len(parts) -1):	
					aDict2[line2[count2]] = word
					count2 = count2 +1
			aDict.append(aDict2)
			aDict2 = {}


client = MongoClient()
db = client.test

db.testcollection.insert_many(aDict)