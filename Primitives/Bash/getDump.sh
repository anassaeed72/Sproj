#! /bin/bash
if [ -z "$1" ]; then
    echo "Please enter virtual machine name"
	exit  1
fi
if [ -z "$2" ]; then
    echo "Please enter dump file name"
	exit  1
fi


sudo dump-memory ${1} ${2}
