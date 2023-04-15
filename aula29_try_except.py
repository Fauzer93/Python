"""
Introdução ao try/except
Try -> tentar executar o código
Except -> Ocorreu algum erro ao tentar executar
"""

# print(1234)
# print(456)
# int('a')

numero_str = input('vou dobrar o número que vc digitou: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_str)
    print('o dobro de {} é {:.2f}' .format(numero_str, numero_float * 2))
except:
    print('Isso não é um número')

#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print('o dobro de {} é {:.0f}' .format(numero_str, numero_float * 2))
#
#else:
#    print('Isso não é um número')