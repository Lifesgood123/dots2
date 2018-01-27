#!/usr/bin/python
from math import sqrt as sroot
from fractions import Fraction
from random import randint
import pylab
import numpy
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("a", type=int)
#parser.add_argument("b", type=int)
#parser.add_argument("c", type=int)
#parser.add_argument("-g", "--graph", help="display graph of function", action="store_true")
#parser.add_argument("-v", "--verbose", help="display more information", action='store_true')

#args = parser.parse_args()

m = float(input("slope> "))
b = float(input("intercept> "))
x = float(input("x> "))

def f(x):
    y = ((m*x)+b)
    print("f("+str(x)+") = "+str(y))
    return y


y = []
x = range(-15, 15)
for i in x:
    y.append(f(i))

pylab.grid(True)
pylab.plot(x,y)
pylab.show()
