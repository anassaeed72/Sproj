import os
import subprocess
import sys
from pymongo import MongoClient
from Print import Print
from Constants import PrintLevel

Print.Print(PrintLevel.Command, "PsList Starting")
proc=subprocess.Popen('python vol.py -f '+sys.argv[1]+' pslist', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
Print.Print(PrintLevel.Command, "PsList Done")
count = 0
index = 0
aDict = []
aDict2 = {}
# line3={'PsList-Offset' :'1','PsList-Name':'keylogger.exe','PsList-PID':'10','PsList-PPID':'100'}
# aDict.append(line3)
# line3={'PsList-Offset' :'1','PsList-Name':'keyloggerxyz.exe','PsList-PID':'10','PsList-PPID':'100'}
# aDict.append(line3)
line2=['PsList-Offset','PsList-Name','PsList-PID','PsList-PPID','PsList-Thds','PsList-Hnds','PsList-Sess','PsList-Wow64','PsList-Start','PsList-Start','PsList-Start','PsList-Exit','PsList-Exit','PsList-Exit','PsList-temp']
# for x in arrayOfFiles:
# 	if os.path.exists(x):
# 		os.remove(x)
# for oneLine in output.split("\n"):
# 	if count < 2:
# 		count = count+1
# 		continue
# 	index = 0
# 	for oneWord in oneLine.split():
# 		commandToExecute= "python AppendToFileNewLine.py " + arrayOfFiles[index] + " " + oneWord
# 		index = index+1
# 		os.system(commandToExecute)

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
if  aDict:
	db.PsListCollection.insert_many(aDict)