#ok, that's *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
   print("arg1: %r, arg2: %r" % (arg1, arg2))

#this just takes one arg
def print_one(arg1):
    print("arg1: %r" % arg1)

#this takes none
def print_none():
    print("I got nuffin'")

print_two_again("Hailey", "Tanner")
print_one("Four Words One String")
print_none()
