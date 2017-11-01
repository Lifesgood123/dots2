from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

currentfile = open(input_file)

print("Here's the whole file: \n")

print_all(currentfile)

print("rewinding mag-tape")

rewind(currentfile)

print("three lines")

i = 1
while i < 4:
    print_a_line(i, currentfile)
    i = i + 1
#fuck yeah nigga!!!!!!!
