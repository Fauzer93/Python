"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostra o 6.')
        continue


    if contador >= 10 and contador <=30:
            #print('contagem pulado do 10 ao 30.')
            continue

    print(contador)

    if contador == 40:
        break


print('Acabou')