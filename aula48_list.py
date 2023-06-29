"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#string = 'ABCDE'# 5 caracteres (len)
# print(bool([])) # false
# print(lista, type(lista))

#..........0...1.........2...........3....4
#..........-5..-4.......-3...........-2...-1
#lista = [123, True, 'fauzer santos', 1.2, []]
#lista[-3] = 'adriano'
#print(lista)
#print(lista[2], type(lista[2]))

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
#lista.append(50)
#lista.pop()
#lista.append(60)
#lista.append(70)
#ultimo_valor = lista.pop() # remove o  valor 
#print(lista, 'removido', ultimo_valor)

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#lista = [10, 20, 30, 40]
#lista.append('fauzer')
#nome = lista.pop()
#lista.append(1233)
#del lista[-1]
#lista.clear()
#lista.insert(0, 'fauzer')
#print(lista)

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#lista_a = [1,2,3]
#lista_b = [4,5,6]
#lista_c = lista_a + lista_b
#lista_d = lista_a.extend(lista_b)
#print(lista_a)
#nome = 'Fauzer'
#outra_variavel = nome
#nome = 'adriano'
#print(nome)
#print(outra_variavel)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

#lista_a = ['fauzer', 'santos',1, True, 1.2]
#lista_b = lista_a.copy()

#lista_a[0] = 'qualquer coisa'
#print(lista_a)
#print(lista_b)