import os
import subprocess
import sys


print 'Argument One:', sys.argv[1]

print 'Argument Two:', sys.argv[2]

proc=subprocess.Popen('python vol.py -f /home/xen/Documents/zeus.vmem pslist', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
print output
