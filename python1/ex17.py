#from sys import argv
#from os.path import exists

#script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")

#in_file = open(from_file)
#indata = in_file.read()

#print(f"The inpu file is {len(indata)} bytes long")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#print("Alright, all done.")

#out_file.close()
#in_file.close()

#---------------------------------------------
# Versão mais curta
#---------------------------------------------
from sys import argv; from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file).read()

print("Hit enter to continue, CTRL-C to cancel it"); input()

out_file = open(to_file, 'w').write(in_file);
