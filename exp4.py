x = "there are %d types of people" % 10 
binary = "binary"
do_not = "don't"
y = "those who know %a and those who %s" % (binary, do_not)

print(x)
print(y)

print("I said: %r" % x)
print("I also said: %s" % y)
hilarious = False
joke_evalution = "wasn't that funny?  %r"
print(joke_evalution % hilarious)
w = "this is the right side of......"
e = "a string with a right side"
print(w + e)