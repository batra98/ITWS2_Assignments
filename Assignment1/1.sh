#!/bin/bash
cat $1 | awk '{if(length($0)>=35){print $0}}' | sed 's/\<in\>/in fact/g'