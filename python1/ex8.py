formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try your",
    "Own text here",
    "maybe a poem",
    "Or a song about fear"
))
print(formatter.format("teste", 2, 4, 8))