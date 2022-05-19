from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("Essa cena ainda não está configurada")
        print("Faça uma subclasse e implemente-a com .enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "Morreu morrido 1"
        "Morreu de maneira morrida 2"
        "Morreu morrendo na morte 3"
        "Morreu enquanto estava sendo morto"
    ]

    def enter(self):
        print(Death.quips[randit(0, len(self.quips)-1)])

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            Blá blá blá Blá blá bláBlá blá bláBlá blá bláBlá blá blá
            Blá blá bláBlá blá bláBlá blá bláBlá blá bláBlá blá blá
            Blá blá bláBlá blá blá
            Blá blá bláBlá blá bláBlá blá bláBlá blá bláBlá blá blá
            Blá blá bláBlá blá bláBlá blá bláBlá blá bláBlá blá bláBlá blá blá
            Blá blá bláBlá blá bláBlá blá blá
        """))
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Morreu de morte morrida sorry! Morreu de morte morrida sorry!
                Morreu de morte morrida sorry! Morreu de morte morrida sorry!
                Morreu de morte morrida sorry!
                Morreu de morte morrida sorry! Morreu de morte morrida sorry!
                Morreu de morte morrida sorry! Morreu de morte morrida sorry!
                Morreu de morte morrida sorry!
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Morreu de maneira patética!  Morreu de maneira patética!
                Morreu de maneira patética! Morreu de maneira patética!
                Morreu de maneira patética! Morreu de maneira patética!
                Morreu de maneira patética!
                Morreu de maneira patética! Morreu de maneira patética!
                Morreu de maneira patética!
            """))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
                Deu sorte e sobreviveu, parabens! Deu sorte e sobreviveu, parabens!
                Deu sorte e sobreviveu, parabens! Deu sorte e sobreviveu, parabens!
                Deu sorte e sobreviveu, parabens!
                Deu sorte e sobreviveu, parabens! Deu sorte e sobreviveu, parabens!
                Deu sorte e sobreviveu, parabens!
                Deu sorte e sobreviveu, parabens! Deu sorte e sobreviveu, parabens!
                Você foi para a laser weapon armory
            """))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            Você tem 10 tentativas pra acertar o código antes de morrer.
            Boa sorte!
        """))

        code = f"{randit(1,9)}{randit(1,9)}{randit(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZED")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                Acertou, vá direto para bridge! Parabens Acertou, vá direto para bridge! Parabens
                Acertou, vá direto para bridge! Parabens
                Acertou, vá direto para bridge! Parabens Acertou, vá direto para bridge! Parabens
                Acertou, vá direto para bridge! Parabens
                Acertou, vá direto para bridge! Parabens
            """))

            return 'the_bridge'

        else:
            print(dedent("""
                Tentativas em excesso, você vai morrer, sinto muito.
                Tentativas em excesso, você vai morrer, sinto muito.
                Tentativas em excesso, você vai morrer, sinto muito.
                Tentativas em excesso, você vai morrer, sinto muito.Tentativas em excesso, você vai morrer, sinto muito.
                Tentativas em excesso, você vai morrer, sinto muito.
            """))

            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            Você entra na ponte com uma bomba na mão e os alienígenas te avistam
            enquanto eles tentavam tomar o controle da bridge, mas não fazem
            nada porque te viram com a bomba na mão, o que você faz?
        """))

        action = input("> ")

        if action == "Joga a bomba":
            print(dedent("""
                Você jogou a bomba no chão e matou todos incluindo você mesmo.
                Você jogou a bomba no chão e matou todos incluindo você mesmo.
                Você jogou a bomba no chão e matou todos incluindo você mesmo.
                Você jogou a bomba no chão e matou todos incluindo você mesmo.
            """))
            return 'death'

        if action == "Ameaça explodir":

            print(dedent("""
                Você ameaça explodir todo mundo e os aliens se rendem, e Você
                calmamente vai indo para a capsula de escape.
                Você ameaça explodir todo mundo e os aliens se rendem, e Você
                calmamente vai indo para a capsula de escape.
                Você ameaça explodir todo mundo e os aliens se rendem, e Você
                calmamente vai indo para a capsula de escape.
                Você ameaça explodir todo mundo e os aliens se rendem, e Você
                calmamente vai indo para a capsula de escape.
            """))
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):

        print(dedent("""
            Você passa pelos aliens e corre em direção às capsulas de escape
             quando se depara com 5 pods, qual você escolhe entrar?
             """))

        good_pod = randit(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:

            print(dedent("""
                Você entrou na capsula {guess} e aprtou o botão de ejetar.
                A capsula vai para o vazio do espaço. A integridade fisica da
                capsula implode esmagando seu corpo.
                 """))
            return 'death'

        else:
            print(dedent("""
            Você entrou na capsula {guess} e aprtou o botão de ejetar.
            A capsula vai para o vazio do espaço. Você se salvou.
            """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won!")
        return 'finished'

class Map(object):

    scenes = {
    'central_corridor' : CentralCorridor(),
    'laser_weapon_armory' : LaserWeaponArmory(),
    'the_bridge' : TheBridge(),
    'escape_pod' : EscapePod(),
    'death' : Death(),
    'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
