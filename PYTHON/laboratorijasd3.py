# -*- coding: utf-8 -*-
from math import sin
import numpy as np
import matplotlib.pyplot as plt

def mans_sinussh(x):
    k = 0
    a = x**1/(1)
    S = a
    while k<500:
        k = k + 1
        R = x**2 /((2*k)*(2*k+1))
        a = a * R
        S = S + a
    return S

a = 2.57 #pi/2 
b = 4.71 #3*pi/2 
x = np.arange(a,b,0.01)
y = np.sinh(x)
yy = mans_sinussh(x)
plt.plot(x,y)
plt.plot (x,yy)
plt.grid()
plt.show()


funa = mans_sinussh(a)
funb = mans_sinussh(b)
if funa * funb > 0:
    print "[%.2f,%.2f] intervala saknes nav"%(a,b)
    print "vai ir paru saknu skaits"
    exit()




    
print "Turpnajums, ja sakne tomer ir:"    
delta_x = 1.e-3 # 1.e3 vs 0.001 vai 1*10^(-3)
k = 0
while b-a > delta_x:
    k = k+1
    x = (a+b)/2
    funx = mans_sinussh(x)
    print "%3d.: a=%.5f f(%.5f)=%8.5f b=%.5f"%(k,a,x,funx,b)
    if funa * funx > 0:
        a = x
    else:
        b = x




print "Gala rezultats:"
print "a=%.5f f(a)=%.5f"%(a,mans_sinussh(a)),
print "x=%.5f f(x)=%.5f"%(x,funx),
print "b=%.5f f(b)=%.5f"%(b,mans_sinussh(b)),
print "Rezultats ir sasniegts %d iteracijas"%(k)