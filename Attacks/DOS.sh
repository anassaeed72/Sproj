#! /bin/bash
declare -A ipAddressHashMap
if [ -z "$1" ]; then
    echo "Please enter virtual machine name"
	exit  1
fi

if [ -z "$2" ]; then
    echo "Please enter min packet count"
	exit  1
fi
echo "Virtual machine name  $1"

# now finding the dump of given vm
echo "Taking MemoryDump"

sudo dump-memory ${1} MemoryDump.mem
# now parsing for finding packets and their info
echo "Parsing Memory Dump for packets"
bulk_extractor -E net -o test MemoryDump.mem 
# copying file to main folder
cp /home/xen/Documents/scripts/test/packets.pcap /home/xen/Documents/scripts/

# getting the packets IP and time
mydata=$(sudo tcpdump -ttttnnr packets.pcap | grep IP)

S1='IP'
S2=' '
one='1' 
test1=${mydata:0:2}
foo=string
for (( i=0; i<${#mydata} -1; i++ )); do
  	test1=${mydata:i:2}
  	ipAddress=''
  	if [ "$test1" == "$S1" ]
 	then
 		for ((j = i+3;j<i+25;j++)); do
 			test2=${mydata:j:1}
 			if [[ "$test2" == "$S2" ]]; then
 				break;
 			fi
 			ipAddress=$ipAddress$test2
 		done
 		if [[ -z "${ipAddressHashMap[$ipAddress]}" ]]; then
 			ipAddressHashMap[$ipAddress]="1"
 		else
 			temp=${ipAddressHashMap[$ipAddress]} 
 			let temp+=$one
 			ipAddressHashMap[$ipAddress]=$temp
 		fi
    	# echo "Final IP Address '$ipAddress'"
    	# values=${ipAddressHashMap[$ipAddress]} 
    	# echo "values is : '$values'"
  	fi
done

# now for implemnting the rule
packetsCount=$2
let packetsCount-=$one
echo $packetsCount
echo "The IPs that are doing DOS attack"
for i in "${!ipAddressHashMap[@]}"
do

	count=${ipAddressHashMap[$i]}
	if [[ "$count" > "$packetsCount" ]]; then
 		echo "IP Address  : $i"
  		echo "Packets count: ${ipAddressHashMap[$i]}"
 	fi

done

echo "All Done. Exiting"