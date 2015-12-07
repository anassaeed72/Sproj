#! /bin/bash
declare -a blackListed=(127.0.0.1 172.16.176.143)

function printIp {
	breaker=':'
	word=$1
  	ipAddress=''
	for (( i = 0; i < ${#word} ; i++ )); do
		oneCharacter=${word:i:1}
		if [[ "$oneCharacter" == "$breaker"  ]]; then
			break
		fi
		ipAddress=$ipAddress$oneCharacter
	done
	echo $ipAddress
	checkForBlacklisted $ipAddress
}

function checkForBlacklisted {
	blackListedString='This Ip is Black Listed : '
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
echo "Connections established in Memory Image"
# vol.py -f ${1} connscan
mydata=$(vol.py -f ${1} connscan)
count='1'
one='1'
two='2'
three='3'
limit="1234567888"
firstTest=''
echo "The IP address connected are the following :"
for word in $mydata
do
	if [[ ${#count}  -gt ${#limit}  ]]; then
		if [[ -z "$firstTest" ]]; then
			firstTest='1'
			continue
		fi
		if [[ "$firstTest" == "$one" ]]; then
			printIp $word &
			firstTest='2'
			continue
		fi
		if [[ "$firstTest" == "$two" ]]; then
			printIp $word &
			firstTest='3'
			continue
		fi
		if [[ "$firstTest" == "$three" ]]; then
			firstTest=''
			continue
		fi
	else
		count=$count$one
	fi
done

wait

