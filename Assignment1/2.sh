#!/bin/bash
awk '{if($3=="apathy"){$3="g1a2u3r4a5v"};{print $0}}' $1 | grep -z "g1a2u3r4a5v" | sed 's/g1a2u3r4a5v/empathy/g'