#Cria uma função de nome(cheese_and_crackers) e nomeia 2 argumentos(cheese_count e boxes_of_crackers)
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #Um simples print que carrega as variaveis da função, que no caso são argumentos
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the functions numbers directly:")
#Chama a função cheese_and_crackers e atribui valores aos dois argumentos que antes estavam vazios
cheese_and_crackers(20,30)


print("OR, we can use variables from our script:")
#Cria duas variaveis de nome aleatório e as carrega nos dois argumentos da chamada da função
amount_of_cheese = 10
amout_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amout_of_crackers)


print("We can even do math inside too:")
#Chama a função e atribui valores aos argumentos só que com uma conta matématica
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amout_of_crackers + 1000)
"""
Teste
"""