import os
import sys
import subprocess

from lxml import etree
import xml.etree.ElementTree

if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()
print "In Multiple Operations"
e = etree.parse(sys.argv[1])
outputOneOperation = ""
def flatten(seq):
  for item in seq:
    if isinstance(item,(etree._Element,)):
    	with open("OneOperationsTempXml.xml", "w") as myfile:
    		myfile.write(etree.tostring(item,with_tail=False))
    		myfile.close()
        os.system('python OneOperation.py OneOperationsTempXml.xml')
  	  	# outputOneOperation = subprocess.check_output(('python OneOperation.py OneOperationsTempXml.xml'),shell=False)
		# if outputOneOperation == "exit\n":
			# print "Exiting system"
			# sys.exit(0)


flatten(e.xpath('/operations/node()'))

