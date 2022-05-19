class Song(object):
    # metódo construtor, vai sempre ser executado quando Song() for chamado
    def __init__(self, lyrics):
        self.lyrics = lyrics
        #self recebe a música de uma instancia

    def sing_me_a_song(self):
        for line in self.lyrics:

            print(line)
# Criação da instancia 1 (objeto 1)
happy_bday = Song(["Happy birthday to you,",
                   "I don't want to get sued",
                   "So I'll stop right there"])

# Criação da instancia2 (objeto 2)
bulls_on_parade = Song(["They rally around tha family.",
                        "With pockts full of shells."])
#
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Pra que serve o self? Como a classe song pode ser utilizada multiplas vezes
# com diferentes valores inseridos na classe por diferentes instancias, como por exemplo a
# música happy_bday e bulls_on_parade, o self serve como uma variavel temporaria
# do objeto.
# então "self.lyrics = lyrics", seria como se fosse "happy_bday.lyrics"
