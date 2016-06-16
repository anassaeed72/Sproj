import os
import subprocess
import sys
from pymongo import MongoClient
from Print import Print
from Constants import PrintLevel
from Constants import ConstantsClass
if len(sys.argv) <2:
	Print.Print(PrintLevel.Error,'Arguments not given')
	sys.exit()
Print.Print(PrintLevel.Command,"DllList Starting")
commandToExecute = 'python vol.py -f ' + sys.argv[1] + " dlllist"
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
Print.Print(PrintLevel.Command, "DllList Ended")
output=proc.communicate()[0]
count = 0
index = 0
aDict = []
aDict2= {}

line2=['DllList-Base','DllList-Size','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path','DllList-Path']

<<<<<<< HEAD
# Print.Print(PrintLevel.RawOuput, output)
=======
Print.Print(PrintLevel.RawOuput, output)
>>>>>>> eecd91e9fd97390d6cb0f1c5da81cdc0f38db5aa


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
Print.Print(PrintLevel.Command,"DllList Added data to DB")