import os
import subprocess
import sys
from pymongo import MongoClient


print "Handles Starting"
proc=subprocess.Popen('python vol.py -f '+sys.argv[1]+' pslist', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
print "Handles Done"
count = 0
index = 0
aDict = []
aDict2= {}

line2=['Handles-Offset','Handles-Name','Handles-PID','Handles-PPID','Handles--Thds','Handles--Hnds','Handles--Sess','PsList-Wow64','PsList-Start','PsList-Start','PsList-Start','PsList-Exit','PsList-Exit','PsList-Exit','PsList-temp']

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

				aDict2[line2[count2]] = word
				count2 = count2 +1

			aDict.append(aDict2)
			aDict2 = {}


client = MongoClient()
db = client.test
db.HandlesCollection.insert_many(aDict)
print "Handles Seeded DB"