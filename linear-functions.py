from fractions import Fraction as frac

def f(m, x, b):
    y = (m*x)+b
    return y
def get_slope(x1, x2, y1, y2):
    m = ((y1-y2)/(x1-x2))
    return m
def get_int(m, x, y):
    b = y - (m*x)
    return b

quest = input("Do you need the slope? y/n  ")

if quest in ["y", "yes"]: 
    x1 = float(input("x1: :"))
    y1 = float(input("y1: :"))
    x2 = float(input("x2: :"))
    y2 = float(input("y2: :"))
    m = get_slope(x1, x2, y1, y2)
    print(frac(m))
    b = get_int(m, x1, y1)
    print(b)
elif quest in ["n", "no"]:
    quest2 = input("Do you need the y intercept?")
    if quest2 in ["y", "yes"]: 
       x = float(input("x: "))
       y = float(input("y: "))
       m = float(input("slope?"))
       b = get_int(m, x, y)
       print(b)
       test_func(m, b)
    elif quest2 in ["n", "no"]:
       x = float(input("x: "))
       y = float(input("y: "))
       m = float(input("slope? "))
       b = float(input("y-intercept: ") 
    else:
        exit
else:
    exit

check = input("check x value? ")
while check in ["y", "yes"]::
    f(m, input("f(?)"), b)
    check = input("again? ")





