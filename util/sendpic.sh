#!/bin/bash

yek=1;
dow=2;
se=3;

if [ $# -lt $yek ];
then
	echo "Please input the image path as an argument"; echo;
	exit 1;
else
	fileheader="file=@"$1;
fi

if [ $# -ge $dow ];
then
	host=$2;
else
	host="http://localhost:8008";
fi

if [ $# -ge $se ];
then
	path=$3;
else
	path="/solve/";
fi

curl -F $fileheader $host$path 2>/dev/null;echo;

if [ $? -ne 0 ]; then
	echo "Curl did not execute properly. try with: "; echo "command path-to-image host path-to-api"; echo;
	exit 1;
fi

