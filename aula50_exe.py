"""
for in com listas
"""

lista = ['Fauzer', 'Adrinao', 'Santos',]
lista.append('Church')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
