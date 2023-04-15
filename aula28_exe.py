"""
Exercício
Peça ao usuário para digita seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:

    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        A primeira letra do seu nome é {letra}
        a última letra do seu nome é {letra}
Se nada for digitado em nome ou idade
    exiba "Desculpe, você deixou campos vazios"
"""

nome = input('Favor informe seu nome: ')
idade = input('Favor informe sua idade: ')

if nome and idade:
    print('Seu nome é {}'.format(nome))
    print('Seu nome invertido é {}'.format(nome[::-1]))

    if ' ' in nome:
        print('seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    
    print('Seu nome tem {} letras'.format(len(nome)))
    print('A primeira letra do seu nome é {}'.format(nome[0]))
    print('A última letra do seu nome é {}'.format(nome[-1]))

else:
    print('Desculpe, você deixou campos vazios')
