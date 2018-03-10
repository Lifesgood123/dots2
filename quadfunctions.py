#!/usr/bin/python
from math import sqrt as sroot
from fractions import Fraction
from random import randint
import pylab
import numpy
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("a", type=str)
parser.add_argument("b", type=str)
parser.add_argument("c", type=str)
parser.add_argument("-g", "--graph", help="display graph of function", action="store_true")
parser.add_argument("-v", "--verbose", help="display more information", action='store_true')

args = parser.parse_args()

def f(x):
    y = (a*(x**2)+(b*x)+c)
    return y

def get_max_min():
    h = float((-1*b)/(2*a))
    k = f(h)
    if a < 0:
        minormax = "max"
    else:
        minormax = "minimum"


def get_x_int(i):
    rooty = sroot(((b**2)-4*a*c))
    if args.verbose:
        print(rooty)
    root1 = (-b + rooty)/(2*a)
    root2 = (-b - rooty)/(2*a)
    if i == 1:
        return root1
    elif i == 0:
        return root2
    else:
            exit
a = float(args.a)
b = float(args.b)
c = float(args.c)

print(get_max_min())
try:
    print(get_x_int(1))
    print(get_x_int(0))
    xint = [str(Fraction((get_x_int(1)))), str(Fraction((get_x_int(0))))]
    for i in xint:
        print(i)
except: 
    print("roots aren't real")
print("I/O check?")
answer = input(">")
while answer == 'y':
    stuff = float(input("> "))
    print(f(stuff))
    answer = input("again? >")



y = []
x = numpy.linspace((150* -1), 150, 100)
for i in x:
    y.append(f(i))
if args.graph:
    pylab.plot(x,y)
    pylab.show()
