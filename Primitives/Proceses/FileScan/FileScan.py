from pymongo import MongoClient
import json
import sys
import os
import subprocess
import sys

# Print.Print(PrintLevel.Command,  "handles Starting ")

# rekal -f windows.mem handles proc_regex= "svchost"
commandToExecute = 'rekal -f ' + sys.argv[1] + " filescan "
proc=subprocess.Popen(commandToExecute, shell=True, stdout=subprocess.PIPE, )
f=proc.communicate()[0]
print "Rekall File Scan"
# Print.Print(PrintLevel.Command,"Handles done")
count = 0
aDict = []
aDict2= {}
#  Offset (V)      Pid     Handle         Access     Type             Details
line2 = ['Rekal-FileScan-Offset', 'Rekal-FileScan-Ptr', 'Rekal-FileScan-Hnd', 'Rekal-FileScan-Acess', 'Rekal-FileScan-Owner', 'Rekal-FileScan-Process-Name','Rekal-FileScan-PID','Rekal-FileScan-FileName']
for line in f.split("\n"):
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
				if count2 >= 7:
					count2 = 7
				aDict2[line2[count2]] = word
				count2 = count2 +1

			aDict.append(aDict2)
			aDict2 = {}

if aDict:
	client = MongoClient()
	db = client.test
	db.fileScanCollection.insert_many(aDict)
print "Done"

#  Offset (V)      Pid     Handle         Access     Type             Details
# -------------- ------ -------------- -------------- ---------------- -------
# 0xe00001f82f20   2628            0x4       0x12019f File             \Device\ConDrv\Reference
# 0xe00001d17e00   2628           0x10       0x100020 File             \Device\HarddiskVolume2\Windows
# 0xe00001f546b0   2628           0x18       0x12019f File             \Device\ConDrv\Input
# 0xe00001eef800   2628           0x1c       0x12019f File             \Device\ConDrv\Output
# 0xe00001eef800   2628           0x20       0x12019f File             \Device\ConDrv\Output
# 0xe00001d0db80   2628           0x24       0x100020 File             \Device\HarddiskVolume2\temp
# 0xe0000006e1f0   2628           0x28       0x12019f File             \Device\ConDrv\Connect
# 0xe00000637480   2628           0x30       0x1f0001 ALPC Port
# 0xe000006bd290   2628           0x34       0x1f0003 Event
# 0xe00001ed6060   2628           0x38            0x1 WaitCompletionPacket
# 0xe00001ecd080   2628           0x3c       0x1f0003 IoCompletion
# 0xe00001ec7060   2628           0x40        0xf00ff TpWorkerFactory
# 0xe00000778320   2628           0x44       0x100002 IRTimer
# 0xe00001ecfb80   2628           0x48            0x1 WaitCompletionPacket
# 0xe00001a629d0   2628           0x4c       0x100002 IRTimer
# 0xe00001ec8f90   2628           0x50            0x1 WaitCompletionPacket
# 0xe00002048970   2628           0x54          0x804 EtwRegistration
# # 0xe0000077dd00   2628           0x58       0x100003 Semaphore
# 0xe00001d1b340   2628           0x5c       0x100001 File             \Device\CNG
# 0xe000006b82c0   2628           0x60       0x100003 Semaphore
# 0xe00001d0c6e0   2628           0x64       0x120196 File             \Device\HarddiskVolume2\temp\win8.1.raw