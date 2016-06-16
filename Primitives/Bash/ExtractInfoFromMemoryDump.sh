#! /bin/bash
if [ -z "$1" ]; then
    echo "Please enter memory dump name"
	exit  1
fi

bulk_extractor -E net -o test ${1} 
