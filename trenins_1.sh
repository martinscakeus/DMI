#!/bin/bash

echo "Ievadi pirmo skaitli:"

read a ;

echo "Ievadi otro skaitli:"

read b ;
echo "a=$a"
echo "b=$b"

if [ $a \> $b ]
then 
    echo "$a Ir lielāks nekā $b"
else
    echo "$b Ir lielāks nekā $a"
fi
