#!/bin/sh
c=0
while [[ $c -lt 20 ]]
do
	./import_normal.py
	let c=c+1
done
