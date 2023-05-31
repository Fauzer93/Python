"""CALCULADORA com While"""

# startswitch - quando preciso que algo seja recohecida pela 1° letra

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um outro número:')
    operador = input('Digite um operador (+ - / *): ')

    num_validos =  None

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



    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
    # print(sair)