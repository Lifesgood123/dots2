formatter = " %s %s %s %s "
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I have this thing.",
    "That you could typr right.",
    "But it didn't sing",
    "So I bid it goodnight"
))