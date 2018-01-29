#!/usr/bin/python
from math import sqrt as sroot
from fractions import Fraction
from random import randint
import pylab
import numpy


def get_slope(p, p1):
    m = (p[1] - p1[1]) /(p[0] - p1[1])
    b = get_int(p, m)
    return m, b

def get_int(p, m):
    b = m * p[0] - p[1] 
    return b

def f(x):
    y = (m*x)+b
    print("f("+str(x)+") = "+str(y))
    return y

def graph():
    y = []
    x = range(-15, 15)
    for i in x:
        y.append(f(i))

    pylab.grid(True)
    pylab.plot(x,y)
    pylab.show()
