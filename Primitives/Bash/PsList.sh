#! /bin/bash
if [ -z "$1" ]; then
    echo "Please dmp file"
	exit  1
fi
if [ -z "$2" ]; then
    echo "Please enter file name"
	exit  1
fi
python vol.py -f ${1} pslist
mydata=$(python vol.py -f ${1} pslist)
len='12345678'
count=''
for word in $mydata
do
	if [[ ${#count} >${#len}  ]]; then
		#statements
		echo $word
	else
		count+='1'
	fi
	

done




# echo ${1} >>${2}