import os
import subprocess
import sys

if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()


# bulk_extractor -E net -o test ${1} 
commandToExecute = 'bulk_extractor -E net -o test '+sys.argv[1]
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
print output

