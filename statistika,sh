#!/bin/bash

a=$1
b=$2
c=$3


if (( $a > $b )) && (( $a > $c )) && (( $b > $c )); then
echo " $a $b $c"
fi
if  (( $a > $b )) && (( $a > $c )) && (( $c > $b )); then
echo "$a $c $b "
fi
if (( $b > $a )) && (( $b > $c )) && (( $a > $c )); then
echo "$b $a $c"
fi
if (( $b > $a )) && (( $b > $c )) && (( $c > $a )); then
echo " $b $c $a"
fi
if  (( $c > $a )) && (( $c > $b )) && (( $a > $b )); then
echo "$c $a $b"
fi
if (( $c > $a )) && (( $c > $b )) && (( $b > $a )); then
echo "$c $b $a"
fi




