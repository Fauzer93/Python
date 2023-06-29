lista = ['Fauzer', 'Adrinao', 'Santos',]
lista.append('Church')

lista_enumerate = list(enumerate(lista))

#print(lista_enumerate)
for item in lista_enumerate:
    indice, nome = item
    print(indice, nome)