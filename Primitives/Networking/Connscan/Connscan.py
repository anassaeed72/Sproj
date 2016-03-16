from pymongo import MongoClient
import json
import sys
import os
import subprocess
import sys
from Print import Print
from Constants import PrintLevel

Print.Print(PrintLevel.Command,  "Connscan Starting ")
commandToExecute = 'python vol.py -f ' + sys.argv[1] + " connscan"
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
f=proc.communicate()[0]

Print.Print(PrintLevel.Command,"Connscan done")
count = 0
aDict = []
aDict2= {}
line2 = ['Connscan-Offset', 'Connscan-Local-Address', 'Connscan-Remote-Address', 'Connscan-Pid']
for line in f.split("\n"):
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

				aDict2[line2[count2]] = word
				count2 = count2 +1

			aDict.append(aDict2)
			aDict2 = {}


client = MongoClient()
db = client.test
db.testcollection.insert_many(aDict)