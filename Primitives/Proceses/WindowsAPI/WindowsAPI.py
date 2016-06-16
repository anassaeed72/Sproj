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
Print.Print(PrintLevel.Command,"WindowsAPI Starting")

commandToExecute = "python vol.py  -f home/xen/Documents/zeus.vmem enumfunc -K"
# proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
Print.Print(PrintLevel.Command, "WindowsAPI Ended")
output = ""
# output=proc.communicate()[0]
# print output
count = 0
index = 0
aDict = []
aDict2= {}

line2=['WindowsAPI-Base','WindowsAPI-Size','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path','WindowsAPI-Path']

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
	pass
	db.WindowsAPICollection.insert_many(aDict)
Print.Print(PrintLevel.Command,"WindowsAPI Added data to DB")