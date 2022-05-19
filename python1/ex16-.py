from sys import argv

script, filename = argv

print(f"Now we're going to read {filename}")

print("Loading...")
target = open(filename, 'r')

print(target.read())
