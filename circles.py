import math
#get variables
coords = input("Center in form of h,k: ")
coord_split = coords.split(',')
h = int(coord_split[0])
k = int(coord_split[1])
r = int(input("radius: "))
# calculate corners
right = h + r
left = h - r
top = k + r 
bottom = k - r
# print 
print("right = (%d, %d)" % (right, k))
print("bottom = (%d, %d)" % (h, bottom))
print("left = (%d, %d)" % (left, k))
print("top = (%d, %d)" % (h, top))