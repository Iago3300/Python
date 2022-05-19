#crie um mapeamento entre estados e siglas
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#Crie um conjunto de estados e algumas cidades deles
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

#Adicione mais algumas cidades
cities['NY'] = 'New York', 'Teste'
cities['OR'] = 'Portland'

#imprima algumas cidades
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#imprima mais alguns estados
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#imprima usando dic state e depois o cities
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#imprima todas as silgas dos estados *******
print('-' * 10)
for state, abbrev in list(states.items()):
    #.items() retorna uma lista com as chaves e seus valores. state(chaves), abbrev(valores)
    print(f"{state} is abbreviated {abbrev}")

#imprima cada cidade no estados
print('-' * 10)
for abbrev, city in list(cities.items()):
    #abbrev é as chaves, city os valores.
    print(f"{abbrev} has the city {city}")

#agora faça ambos ao mesmo tempo
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#com segurança, obtenha uma sigla de um estado que pode não estar California
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#obtenha uma cidade com um valor padrãoptimize
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")
