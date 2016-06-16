import os
import subprocess
import sys

if len(sys.argv) <3:
	print('Arguments not given')
	sys.exit()


commandToExecute = 'sudo dump-memory ' + sys.argv[1] +' ' + sys.argv[2]
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
print output

