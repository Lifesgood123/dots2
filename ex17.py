from sys import argv 
from os.path import exists

script, from_file, to_file = argv

print("coping from %s to %s" % (from_file, to_file))

#how do I do this in one line
in_file = open(from_file)
indata = in_file.read()

print("this file is %d bytes long" % len(indata))

print("does the output file exist? %r " % exists(to_file))
print("hit return to countinue")
input(">")
out_file = open(to_file, 'w')
out_file.write(indata)

print("finished")

out_file.close()
in_file.close()

