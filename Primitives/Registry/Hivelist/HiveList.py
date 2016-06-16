import os
import subprocess
import sys

if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()


commandToExecute = 'python vol.py -f ' + sys.argv[1] + " hivelist"
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
count = 0
index = 0
arrayOfFiles=['Virtual.txt','Physical.txt','Name.txt']

for x in arrayOfFiles:
	if os.path.exists(x):
		os.remove(x)
for oneLine in output.split("\n"):
	if count < 2:
		count = count+1
		continue
	index = 0
	commandToExecute= "python NewLine.py Name.txt"
	os.system(commandToExecute)
	for oneWord in oneLine.split():
		if index>1:
			commandToExecute= "python AppendToFile.py Name.txt " + oneWord
			os.system(commandToExecute)
			continue
		commandToExecute= "python AppendToFileNewLine.py " + arrayOfFiles[index] + " " + oneWord
		os.system(commandToExecute)
		index = index+1

