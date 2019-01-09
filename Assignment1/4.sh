#!/bin/bash
cat $1 | awk -F ":" '{print "USER #"NR"="$1}'