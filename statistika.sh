#!/bin/bash

a=$1
b=$2
c=$3


if (( $a > $b )) && (( $a > $c )) && (( $b > $c )); then
echo " max=$a  min=$c"
fi
if  (( $a > $b )) && (( $a > $c )) && (( $c > $b )); then
echo "max=$a  min=$b "
fi
if (( $b > $a )) && (( $b > $c )) && (( $a > $c )); then
echo "max=$b  min=$c"
fi
if (( $b > $a )) && (( $b > $c )) && (( $c > $a )); then
echo " max=$b  min=$a"
fi
if  (( $c > $a )) && (( $c > $b )) && (( $a > $b )); then
echo "max=$c  min=$b"
fi
if (( $c > $a )) && (( $c > $b )) && (( $b > $a )); then
echo "max=$c  min=$a"
fi




