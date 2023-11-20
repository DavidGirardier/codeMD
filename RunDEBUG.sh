#!/bin/bash

rm fort.111
rm multipleTraj.txt
touch multipleTraj.txt
for FRACTION in {1..100}
do

	../../bin/optle
	cat fort.111 >> multipleTraj.txt
done
