from sys import argv 
from os.path import exists

script, from_file, to_file = argv

#how do I do this in one line
in_file = open(from_file)
indata = in_file.read()

print("this file is %d bytes long" % len(indata))

print("does the output file exist? %r " % exists(to_file))


out_file = open(to_file, 'w')
out_file.write(indata)

print("finished")

out_file.close()
in_file.close()

