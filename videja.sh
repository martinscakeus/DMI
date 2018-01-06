#!/bin/bash

a=$1
b=$2
c=$3



var1= $((( $a+$b+$c )/3))
#var2= $(((( $a+$b+$c )%3)*10/3))
echo "$var1.$var2"
