import os
import subprocess
import sys
from pymongo import MongoClient

if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()
print "DllList Starting"
commandToExecute = 'python vol.py -f ' + sys.argv[1] + " dlllist"
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
print "DllList Ended"
output=proc.communicate()[0]
print "Got output"
count = 0
index = 0
aDict = []
aDict2= {}

line2=['DllList-Base','DllList-Size','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path']

# print output


for line in output.split("\n"):
	count = count +1
	if count == 1:
		continue
	else:
		if count > 2:
			line = line.strip()
			parts = line.split("\t")
			parts = parts[0].split()
			count2 = 0
			for word in parts:
				if count2 >10:
					count2 = 10
				aDict2[line2[count2]] = word
				count2 = count2 +1

			aDict.append(aDict2)
			aDict2 = {}


client = MongoClient()
db = client.test
if aDict:
	db.DllListCollection.insert_many(aDict)
print "Added data to DB"