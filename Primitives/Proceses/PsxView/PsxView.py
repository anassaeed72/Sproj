import os
import subprocess
import sys
from pymongo import MongoClient
from Print import Print
from Constants import PrintLevel



Print.Print(PrintLevel.Command, "PsxView Starting")
proc=subprocess.Popen('python vol.py -f '+sys.argv[1]+' psxview', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
Print.Print(PrintLevel.Command, "PsxView Done")
count = 0
index = 0
aDict = []
aDict2= {}

line2=['PsxView-Offset','PsxView-Name','PsxView-PID','PsxView-pslist','PsxView-psscan','PsxView-thrdproc','PsxView-pspcdid','PsxView-csrss','PsxView-session','PsxView-deskthrd','PsxView-ExitTime']


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
	db.PsxViewCollection.insert_many(aDict)
print ("PsxView Data added to DB")