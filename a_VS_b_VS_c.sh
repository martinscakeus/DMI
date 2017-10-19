
#!/bin/bash

echo "Input a: "; read a
echo "Input b: "; read b
echo "Input c: "; read c
if (( $a > $b )) && (( $a > $c ))
then
echo " Skaitlis a ($a) ir vislielākais"



elif  (( $b > $a )) && (( $b > $c ))
then 
echo "Skaitlis b ($b) ir vislielākais"
elif (( $c > $a )) && (( $c > $b ))
then 
echo "Skaitlis c ($c) ir vislielākais"
if (( $b > $c ))
then
echo " $a $b $c"
fi










: <<'END'
if (( $a == $b ))
then
echo "a ($a) ir vienāds ar b ($b)"
fi

if (( $a > $b ))
then
echo "a ($a) ir lielāks par b ($b)"
fi

if (( $a < $b ))
then
echo "a ($a) ir mazāks par b ($b)"
fi
END

: <<'END'
c=`expr $a + $b`
echo "$a + $b = "$c
END
