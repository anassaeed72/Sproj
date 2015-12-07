#! /bin/bash
if [ -z "$1" ]; then
    echo "Please dmp file"
	exit  1
fi
if [ -z "$2" ]; then
    echo "Please enter file name"
	exit  1
fi
mydata=$(python vol.py --profile=Win7SP0x86 -f ${1} pslist)
echo $mydata
for word in $mydata
do
	# echo $word

done




# echo ${1} >>${2}