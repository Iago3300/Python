print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newLines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n\t the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere the is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
#Essas 3 variavéis abaixo não tem ligação com as variaveis da função secret_formula,
# são 3 variaveis sem valor nenhum cujo o unico proposito é receber o retorno da função.
#Os valores retornados da função em ordem: 1º jelly_beans, 2º jars, 3º crates será
# retornado nas variaveis de qualquer nome que você nomeou em ordem.
# Se colocar "jars, beans, crates", ao invés de "beans, jars, crates", o valor
# de jelly_beans será depositado em jars, porque no retorno da função,
# jelly_beans é o 1º valor retornado.

beans, jars, crates = secret_formula(start_point)



print("With a start point of: {}".format(start_point))

print(f"We'd have {beans}, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
