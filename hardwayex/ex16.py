from sys import argv

script, filename = argv

print("We are going to erase %r" % filename)
print("If you don't want this hit ctrl-C(^C)")
print("if this is fine, hit RETURN")

input("?")

print ("Opening file.......")
target = open(filename, mode='w')

print("truncating the file")
target.truncate()

print("Now I will ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm gonna write these to the file")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("closing...")
target.close()
