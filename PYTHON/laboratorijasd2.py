# -*- coding: utf-8 -*-

from math import sinh


def mans_sinussh(x):
    k = 0
    a = x**1/(1)
    S = a
    while k<10:
        k = k + 1
        R = x**2 /((2*k)*(2*k+1))
        a = a * R
        S = S + a
        print (k,a)
    return S




x = 1. *  input("Lietotāj, lūdzu ievadi argumentu (x):")
print type(x)
y = sinh(x)
print "standarta sinh(%.2f)=%.2f"%(x,y)

yy = mans_sinussh(x)
print "mans sinh(%.2f)=%.2f"%(x,yy)
