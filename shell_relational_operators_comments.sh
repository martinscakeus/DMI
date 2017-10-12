#!/bin/bash

a=10
b=20


# 3.piemērs 
echo "Vai skaitlis $a nav vienāds ar skaitli $b?"
if [ $a -ne $b ]
then 
echo "Jā, $a un $b nav vienādi skaitļi"
else 
echo "Nē, $a un $b ir vienādi skaitļi"
fi











: <<'END'
# 2.piemērs - salidzināšana - vai ir vienāds (operācija ==)
echo "----------2.piemērs ----------" # parādās jebkurā gadījumā
echo "Vai skaitlis $a ir vienāds ar skaitli $b" # -"-
if [ $a == $b ]
then
echo "Jā" # tikai ja atbilde uz jautājumu vai a ir vienāds ar b ir TRUE
echo "$a un $b ir vienādi skaitļi" # -"-
else
echo "Nē" # tikai ja atbilde uz jautājumu vai a ir vienāds ar b ir FALSE
echo "$a un $b ir dzažādi skaitļi" # -"-
fi
echo "------------------------------" # parādīsies jebkurā
END


: <<'END' # komentāra bloka sākums
# 1.piemērs - salidzināšana - vai ir vienāds (atslēga -eq)
echo "----------1.piemērs ----------" # parādās jebkurā gadījumā
echo "Vai skaitlis $a ir vienāds ar skaitli $b" # -"-
if [ $a -eq $b ]
then
echo "Jā" # tikai ja atbilde uz jautājumu vai a ir vienāds ar b ir TRUE
echo "$a un $b ir vienādi skaitļi" # -"-
else
echo "Nē" # tikai ja atbilde uz jautājumu vai a ir vienāds ar b ir FALSE
echo "$a un $b ir dzažādi skaitļi" # -"-
fi
echo "------------------------------" # parādīsies jebkurā
END
# komentāra bloka beigas

