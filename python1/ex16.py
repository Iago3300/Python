from sys import argv

script, filename = argv

print(f"If we're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit return.")

input("?")

print("Opening the file...")
target = open(filename, 'w') #'w' é o parametro pra ler, é W de write, há tbm r de read(ler) e a(anexar)

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to right these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally, we close it.")
target.close()
