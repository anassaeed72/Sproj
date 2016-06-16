#! /bin/bash
if [ -z "$1" ]; then
    echo "Please enter data"
	exit  1
fi
if [ -z "$2" ]; then
    echo "Please enter file name"
	exit  1
fi

echo ${1} >>${2}