from sys import argv
script, filename = argv
#open the file 
txt = open(filename)
print("here's your file %r:" % filename, end='\n\n' )
print("..........................", end='\n\n')
#print contents of file to screen
print(txt.read())
#close the file 
txt.close()
print("..........................")