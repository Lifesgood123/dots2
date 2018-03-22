from math import sqrt

def trans(x):
    points = []
    
    points.append((x-c)/b)
    points.append(a*f((x-c)/b)+d)
    
    return points

def f(x):
    return sqrt(x**2)
nums = []
for i in range(-10, 11):
    nums.append(i)

a = float(input('a> '))
b = float(input('b> '))
c = float(input('c> '))
d = float(input('d> '))

newnums = []

for i in nums:
    newnums.append(trans(i))

oldnums = []
meh = []
for i in nums:
    meh.append(i)
    meh.append(f(i))
    oldnums.append(meh)
    meh = []

for i in oldnums:
    print(i)

print('\n')


for i in newnums:
    print(i)
