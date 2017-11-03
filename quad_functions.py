def f(a, b, c, x):
    y = (a*(x**2)+(b*x)+c)
    print("f(%d) = %d" % (x, y))
    return y

def get_max_min(a, b, c):
    h = float((-1*b)/(2*a))
    k = f(a, b, c, h)
    if a < 0:
        minormax = "max"
    else:
        minormax = "minimum"
    print("%s is (%r, %r)" % (minormax, h, k))

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

get_max_min(a, b, c)

print("I/O check?")
answer = input(">")

if answer == "y":
    i = 0
    while i < 1:
        x = float(input("f(?)"))
        y = f(a, b, c, x)
        answer2 = input("more?")
        if answer2 == "y":
            i = 0
        else:
            i = 1
else:
    exit
