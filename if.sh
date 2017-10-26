#!/bin/bash
#if (...) then ....elif(...)then..... else ... fi

a=$1
if (( $a > 0 ))
then

   echo "Izdruka no galvenā zara (Jā gadījumā),tad,kad $a ir lielāks par 0"
elif (( $a == 0 ))
then
echo "Izdruka no galvenā zara (Jā gadījumā),tad,kad $a ir vienādds ar 0" 

else
echo "Izdruka no galvenā zara (Jā gadījumā),tad,kad $a nav lielāks par 0" 
echo "Nostrādā tad, kad iestājas nē gadījums visos iepriekšējos gadījumos."
fi
echo "šis teksts tiks atetēlots Jebkurā gadījumā!"






: <<'END'
a=$1
if (( $a > 0 ))
then

   echo "Izdruka no galvenā zara (Jā gadījumā),tad,kad $a ir lielāks par 0"
else
echo "Izdruka no galvenā zara (Jā gadījumā),tad,kad $a nav lielāks par 0" 
fi
echo "šis teksts tiks atetēlots Jebkurā gadījumā!"
END








: <<'END'
#if (...) then  .... fi
a=$1
if (( $a > 0 ))
then

   echo "Izdruka no galvenā zara (Jā gadījumā),tad,kad $a ir lielāks par 0"
fi
echo "šis teksts tiks atetēlots Jebkurā gadījumā!"
END
