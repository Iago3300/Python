import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Faça uma classe chamada %%% que é %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "A classe %%% tem um __init__ que recebe self e *** de parametross",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "A classe %%% tem uma funcção *** que recebe self e @@@ de parametros",
    "*** = %%%()":
        "Defina *** para uma instancia da classe %%%.",
    "***.***(@@@)":
        "A partir de *** pegue a função *** e chame-a com os parametros self e @@@.",
    "***.*** = '***'":
        "A partir de *** pegue o atributo *** e define-o como '***'."
}

# quer treinar primeiro as frases ou os nomes?
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# carregue as palavras do website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                 random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        #nomes de classes falsos
        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# continue executando até que seja digitado o CTRL-D (CTRL-C no windows)
try:
    while True:
        snippets = list(PHRASES.keys())
        # returns a randomly shuffled dictionary keys list
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye")
