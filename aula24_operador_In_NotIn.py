# Operador in e not in
# Strings são iteráveis (navegar um por um)
# 0 1 2 3 4 5
# F a u z e r 
#-6-5-4-3-2-1

nome = 'Fauzer'
print(nome[2])
print(nome[-4])
print('u' in nome)
print('o' in nome)
print(10 * '-')
print('u' not in nome)
print('o' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que Deseja encontrar: ')

if encontrar in nome:
    print('{} está em {}'.format(encontrar, nome))
else:
    print('{} não está em {}'.format(encontrar, nome))