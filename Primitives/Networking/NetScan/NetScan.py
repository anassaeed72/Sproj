import os
import subprocess
import sys

if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()


commandToExecute = 'python vol.py -f ' + sys.argv[1] + " netscan"
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
count = 0
index = 0
arrayOfFiles=['Offset.txt','Proto.txt','Local-Address.txt','Foriegn-Address.txt','State.txt','Pid.txt','Owner.txt','Created.txt', 'Created.txt', 'Created.txt']
for x in arrayOfFiles:
	if os.path.exists(x):
		os.remove(x)
for oneLine in output.split("\n"):
	if count < 2:
		count = count+1
		continue
	index = 0
	for oneWord in oneLine.split():
		commandToExecute= "python AppendToFileNewLine.py " + arrayOfFiles[index] + " " + oneWord
		index = index+1
		os.system(commandToExecute)

