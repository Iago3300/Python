from sys import exit
#Função pra entrar na sala final
def gold_room():
    print("This room is full of gold. How much do you take?")
    #Usuario digita o valor, input recebe e guarda na variavel choice
    choice = input("> ")
    # Se digitado 0 ou 1, um desses valores é atribuido a variavel how much
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    #Qualquer outra coisa digitado chama a função dead que encerra o script
    else:
        dead("Man, learn to type a number")
    #S e o input for menor que 50 vai printar o que abaixo
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    # Senão chama a função dead pra encerrar
    else:
        dead("You greedy fucker!")
#Função para entrar na sala do urso
def bear_room():
    print("There a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
    # While true cria um loop infinito até o Usuario escolher a opção certa, toda vez
    # que digita algo que não seja "take honey ou taunt bear" o if vai cair no
    # else, que só tem um print(), scrip vai terminar e recomeçar por causa do while.
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps you face off.")
        # Se o input for taunt bear(True) and NOT false(True)
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("you can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews you leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "open door" and not bear_moved:
            dead("You try opening the door and the bear mauls you alive.")
        else:
            print("I got no idea of what that means.")



def cthulhu_room():
    print("Here you see the greater evil Cthulhu.")
    print("He, it, whatever it is stares at you, and you go insane.")
    print("Do you flee for you life or eat you head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There's a door to you right and to your left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve to death.")

start()
