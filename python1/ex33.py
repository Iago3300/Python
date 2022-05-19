#Execercicio
numbers = []

def enquanto(Nome_qualquer, i):#Nome_qualquer é a variavel temporária.

    while i < Nome_qualquer:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

enquanto(6, 1)
# 6(Nome_qualquer) 1(i)

print("The number: ")

for num in numbers:
    print(num)
#*************************************************************
print('*' * 14)
## original
#i = 0
#numbers = []
#
#while i < 6:
#    print(f"At the top i is {i}")
#    numbers.append(i)
#
#    i = i + 1
#    print("Numbers now: ", numbers)
#    print(f"At the bottom i is {i}")
#
#print("The number: ")
#
#for num in numbers:
#    print(num)
