#! /bin/bash

if [ -z "$1" ]; then
    echo "Please enter memory image name"
	exit  1
fi

echo "Memory Image Info"
vol.py -f ${1} imageinfo



