from pymongo import MongoClient
import json
import sys
import os
import subprocess
import sys
from Print import Print
from Constants import PrintLevel
import yara

def mycallBack(data):
	print data
	yara.CALLBACK_CONTINUE



Print.Print(PrintLevel.Command,  "Yara Starting ")
rules = yara.compile('crypto.yar')
matches=  rules.match(sys.argv[1])
print matches
# commandToExecute = "yara -r main.yara "+sys.argv[1]
# proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
# f=proc.communicate()[0]
# print f
Print.Print(PrintLevel.Command,"Yara done")
