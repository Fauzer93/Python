"""CALCULADORA com While"""

# startswitch - quando preciso que algo seja recohecida pela 1° letra

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um outro número:')
    operador = input('Digite um operador (+ - / *): ')

    num_validos =  None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print('Um dos números são invalidos.')
        continue

    operador_permitidos = '+-/*'
    if operador not in operador_permitidos:
        print('Operador Inválido')

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=',num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria chega aqui')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
    # print(sair)