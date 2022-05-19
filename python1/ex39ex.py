estados = {
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Paraná': 'PR',
    'Minas Gerais': 'MG'
}

cidades = {
    'SP': ['São Paulo', 'Campinas'],
    'RJ': ['Rio de Janeiro' 'Cidade de Deus'],
    'PR': ['Curitiba' 'Londrina'],
    'MG': ['Belo Horizonte' 'Ouro Preto']
}

cidades['RS'] = 'Porto Alegre', 'Gramado'
estados['Rio Grande do Sul'] = 'RS'

print('-' * 75)
print("Um novo estado foi adicionado:", estados['Rio Grande do Sul'])
print("As cidades de RS são: ", cidades['RS'])

print('-' * 75)

print("A seguir as listas dos estados:")
#.items() retorna uma lista com as chaves e seus valores. state(chaves), abbrev(valores)
for estados, siglas in list(estados.items()):
    print(f"{siglas} é a abreviação de {estados}")
print('-' * 20)
