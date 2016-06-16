import os
import subprocess
import sys
from pymongo import MongoClient
from Print import Print
from Constants import PrintLevel

Print.Print(PrintLevel.Command, "Psscan Starting")
commandToExecute = 'python vol.py -f ' + sys.argv[1] + " psscan"
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
Print.Print(PrintLevel.Command, "Psscan Ended")
output=proc.communicate()[0]
count = 0
index = 0
aDict = []
aDict2= {}

line2=['Psscan-Offset','Psscan-Name','Psscan-PID','Psscan-PPID','Psscan-PDB','Psscan-Time-Created','Psscan-Time-Created','Psscan-Time-Created','Psscan-Time-Exited','Psscan-Time-Exited','Psscan-Time-Exited']


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
	db.PsscanCollection.insert_many(aDict)
print("Psscan Added to DB")