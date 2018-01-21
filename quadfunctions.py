from math import sqrt as sroot
from fractions import Fraction
from random import randint
import pylab
import numpy


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
    if (b**2)-(4*a*c) < 0:
        print("""
        roots aren't real, Now this will crash
        """)
        input(">")
    rooty = sroot(((b**2)-4*a*c))
    root1 = (-b + rooty)/(2*a)
    root2 = (-b - rooty)/(2*a)
    if i == 1:
        return root1
    elif i == 0:
        return root2
    else:
        exit

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print(get_max_min())
print(get_x_int(1))
print(get_x_int(0))
xint1 = str(Fraction((get_x_int(1))))
xint2 = str(Fraction((get_x_int(0))))
print("I/O check?")
answer = input(">")
y = []
x = numpy.linspace(-15,15,100)
for i in x:
    y.append(f(i))

pylab.plot(x,y)
pylab.show()
