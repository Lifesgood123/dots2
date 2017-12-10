from sys import argv

i = 0
numbers = []

while i < int(argv[1]):
    print("top of loop i is %d" % i)
    numbers.append(i)
    i = i + 1
    for num in numbers:
        print("includes %d" % num)
    print("bottom of loop i is %d" % i)
print(numbers)
print("array is " + str(len(numbers)) + " numbers long")

