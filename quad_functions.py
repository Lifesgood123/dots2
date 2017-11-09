from math import sqrt as sroot
from fractions import Fraction 

def f(a, b, c, x):
    y = (a*(x**2)+(b*x)+c)
    print("f(%d) = %d \n " % (x, y))
    return y

def get_max_min(a, b, c):
    h = float((-1*b)/(2*a))
    k = f(a, b, c, h)
    if a < 0:
        minormax = "max"
    else:
        minormax = "minimum"
    print("%s is (%r, %r) \n " % (minormax, h, k))


def get_x_int(a, b, c, i):
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

get_max_min(a, b, c)
xint1 = str(Fraction((get_x_int(a, b, c, 1))))
xint2 = str(Fraction((get_x_int(a, b, c, 0))))
print ("x intercepts  = %s, %s \n" % (xint1, xint2))
print("I/O check?")
answer = input(">")

while answer == "y":
    x = float(input("f(?)"))
    y = f(a, b, c, x)
exit
