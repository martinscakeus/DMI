# -*- coding: utf-8 -*-
from math import sin
import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x):
    k = 0
    a = (-1)*x**1/(1)
    S = a
    while k<500:
        k = k + 1
        R = (-1)*x**2 /((2*k)*(2*k+1))
        a = a * R
        S = S + a
    return S

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

a = 1.57 #pi/2
b = 4.71 #3*pi/2
x = np.arange(a,b,0.01)
y = mans_sinuss(x)
yy = mans_sinussh(x)
plt.plot(x,y)
plt.plot (x,yy)
plt.grid()
plt.show()


