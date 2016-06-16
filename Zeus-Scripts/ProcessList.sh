#! /bin/bash
declare -a blackListed=( VMwareTray.exe )

function printProcess {
	addressString='The address is : '
	nameString=' Process name is : '
	input=$1
	address=${input:0:10}
	echo $addressString$address
	address=${input:11:${#input}-11}
	echo $nameString$address
	checkForBlacklisted $address
}
function checkForBlacklisted {
	blackListedString='This process is Black Listed : '
	for i in "${blackListed[@]}"
	do
		if [[ $i == $1 ]]; then
			echo $blackListedString$1
			break
		fi
	done
}

if [ -z "$1" ]; then
    echo "Please enter memory image name"
	exit  1
fi

echo "Process List in Memory Image"
mydata=$(vol.py -f ${1} pstree)
count='1'
one='1'
two='2'
three='3'
four='4'
five='5'
six='6'
seven='7'
dot='.'
limit="123456788888"
firstTest=''
echo "The Processes are the following :"
for word in $mydata
do
	if [[ ${#count}  -gt ${#limit}  ]]; then
		# echo $word
		# echo $firstTest
		# echo $dot$dot$dot
		isFirstDot=${word:0:1}
		if [[ "$isFirstDot" == "$dot" ]]; then			
			continue
		fi
		if [[ -z "$firstTest" ]]; then
			printProcess $word &
			firstTest='1'
			continue
		fi
		if [[ "$firstTest" == "$one" ]]; then			
			firstTest='2'
			continue
		fi
		if [[ "$firstTest" == "$two" ]]; then
			firstTest='3'
			continue
		fi
		if [[ "$firstTest" == "$three" ]]; then
			firstTest='4'
			continue
		fi
		if [[ "$firstTest" == "$four" ]]; then
			firstTest='5'
			continue
		fi
		if [[ "$firstTest" == "$five" ]]; then
			firstTest='6'
			continue
		fi
		if [[ "$firstTest" == "$six" ]]; then
			firstTest='7'
			continue
		fi
		if [[ "$firstTest" == "$seven" ]]; then
			firstTest=''
			continue
		fi
	else
		count=$count$one
	fi
done

