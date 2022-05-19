from sys import exit

def dark_room():
    print("""
Você entrou numa sala misteriosa e a sua frente você vê 3 portas, qual porta você
escolhe entrar? O da esquerda, o da direita ou o do centro?""")

    choice = input("> ")

    if "esquerda" in choice:
        trap_room3()

    elif "direita" in choice:
        bear_room()

    elif "centro" in choice:
        room3()

    else:
        death("Não reconheço essa resposta.")


def bear_room():
    print("""
Você entra na porta direita, anda até o final do corredor e se
depara com um urso enorme comendo um pote de mel, atrás dele há uma porta.

O que você faz?""")
    print("""
    1. Assusta o urso
    2. Pega o pote de mel
    3. Ataca o urso
    4. Voltar""")

    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "assusta o urso" and not bear_moved:
            print("Você grita e se faz parecer grande e espanta o urso da porta.")
            print("Com o caminho livre o que você faz? 'voltar' ou 'abrir a porta' ")
            bear_moved = True
        elif choice == "abrir a porta" and bear_moved:
            trap_room1()
        elif choice == "pega o pote de mel":
            death("Você tenta roubar o mel do urso e ele te estraçalha de raiva.")
        elif choice == "Ataca o urso":
            death("Você dá socos e pontapés no urso que se defende ferozmente e te mata.")
        elif choice == "voltar":
            dark_room()
        else:
            print("Comandos: assusta o urso, pega o pote de mel, ataca o urso, voltar")




def trap_room1():
    print("""
Você entrou numa sala com duas portas.
A porta da esquerda aparenta estar nova e em boas condições, indicando que poucas
pessoas passaram por ali.
A porta da direita aparenta estar bem velha e suja indicando que muita gente usa
aquela porta.

O que você faz?""")
    print("""
    1. Esquerda
    2. Direita""")

    choice = input("> ")

    if "esquerda" in choice:
        trap_room2()
    elif "direita" in choice:
        death("Você abre a porta menos suspeita e cai num buraco de 50 metros e morre.")
    else:
        print("Não sei o que ques dizer. Comandos: 'esquerda' ou 'direita'")
        trap_room1()

def trap_room2():
    print("""
Você entra em outra sala e se depara com um aviso escrito na parede:

    "A ganância pelo dinheiro deixa as pessoas cegas ao que está diante dos seus olhos"

Há duas portas na sala, a porta em frente diz "Caminho curto ao seu destino final",
a porta a esquerda diz "Caminho longo ao seu destino final"

O que você faz?""")
    print("""
    1. Frente
    2. Esquerda""")

    choice = input("> ")

    if frente in choice:
        death("""
Você entra na sala e a porta se fecha sozinha. Na parede está escrito:
        "Eis o caminho mais curto para a sua morte!" """)
    elif "esquerda" in choice:
        big_hall()
    else:
        print("Não sei o que ques dizer. Comandos: 'frente' ou 'esquerda'")
        trap_room2()

def trap_room3():
    print("""
Você entra numa sala pouco iluminada e com um cheiro muito forte, há somente uma
porta na sala.

O que você faz?
""")
    print("""
    1. Abre a porta
    2. Volta""")

    choice = input("> ")

    if "abre a porta" in choice:
        death("""
O cheiro terrivel eram os corpos de outros aventureios, e no fundo da sala você
vê um espirito que te mata instantaneamente.""")
    elif "volta" in choice:
        dark_room()
    else:
        print("Não sei o que ques dizer. Comandos: 'abre a porta' ou 'volta'")
        trap_room3()

def room3():
    print("""
Você entra numa sala com 3 plataformas suspensas e na parede escrito
"Duas escolhas são morte certa, uma o sucesso."

Qual plataforma você pula?
""")
    print("""
    1. Esquerda
    2. Meio
    3. Direita
    4. Volta""")

    choice = input ("> ")

    if "esquerda" in choice:
        death("Você pula na plataforma esquerda e cai num buraco cheio de espinhos e morre.")
    elif "direita" in choice:
        death("Você pula na plataforma direita e ativa um mecanismo que atira 3 flechas no seu peito te matando na hora.")
    elif "meio" in choice:
        print("Você pula na plataforma do meio e nada acontece. Com isso você prossegue e abre a porta adiante.")
        big_hall()
    elif "volta" in choice:
        dark_room()
    else:
        print("Não sei o que ques dizer. Comandos: 'esquerda', 'direita' ou 'meio'.")
        room3()

def big_hall():
    print("""
Você entra numa sala enorme com duas portas de ouro massiço. A porta a sua direita tem
rastros de sangue.
A porta a sua esquerda está relativamente brilhante, quase invitativo

O que você faz?""")

    print("""
    1. Frente
    2. Esquerda""")

    choice = input("> ")

    if "frente" in choice:
        death_gold()
    if "esquerda" in choice:
        gold_room()

def death_gold():
    print("""
Você entra na sala de ouro e se alegra com o tanto de metal amarelo que vê na
sua frente, quando você pega uma das moedas a porta atrás de você se tranca e
um gás misterio começar a sair da parede, é um gás venenoso, em pouco tempo você
colapsa e morre.
 """)
    exit(0)

def gold_room():
    print("""
Você entra na sala de ouro e se surpreende com o que vê, uma única moeda é achada no
chão, e de baixo dela um papel com os dizeres:

    "O maior prêmio você pode levar deste lugar é a sua vida, não deixe a ganância
                        tomar conta de ti. Boa sorte."
 """)

def death(room_print):
    print(room_print, "Fim!")
    exit(0)

dark_room()
