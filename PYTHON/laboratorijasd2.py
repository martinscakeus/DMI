# -*- coding: utf-8 -*-

from math import sinh



print "   500"
print "   -----------"
print "   \ "
print "    \                  2*k+1"
print "     \               X"
print"s(x)=|    -----------------------------"
print "     /            (2*k+1)!"
print "    / "
print "   / "
print "   -----------"
print "   k=0"
print
print
print




print "                          2"
print "                        x"
print "         R=   --------------------"
print "                   (2*k) (2*k+1)"







def mans_sinussh(x):
    k = 0
    a = x**1/(1)
    print ("Pirmais saskaitāmais: a%d = %6.2f")%(k,a)
    S = a
    while k<500:
        k = k + 1
        R = x**2 /((2*k)*(2*k+1))
        a = a * R
        S = S + a
        if k>=499:
           print (" a%d = %6.2f")%(k,a)
           
        
              
    return S





x = 1. *  input("Lietotāj, lūdzu ievadi argumentu (x):")
print type(x)
y = sinh(x)
print "standarta sinh(%.2f)=%.2f"%(x,y)

yy = mans_sinussh(x)
print "mans sinh(%.2f)=%.2f"%(x,yy)
