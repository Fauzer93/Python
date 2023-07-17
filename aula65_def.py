"""
Introdução ás funções (def) em python
Funcções são trechos de código usados para 
replicar determinada ação ao longoi do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor especifico.
Por padrão funcções python retornam None (nada)
"""


#def Print(a, b, c):
#    print('Várias1')
#    print('Várias2')
#    print('Várias3')
#    print('Várias4')

#def imprimir(a, b, c):
#    print(a, b, c)

#imprimir(1, 2, 3)
#imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Fauzer')
saudacao('Adriano')
saudacao('Jose')
saudacao()