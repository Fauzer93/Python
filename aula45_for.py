"""
Iterável -> str, range, etc (___ter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

#texto = iter('Fauzer') #__iter__
#print(texto)

#numeros = range(0, 100, 8)
#for numero in numeros:
#    print(numero)

texto = 'Fauzer' #Iterável
#iterador = iter(texto) # Iterador

#while True:
#    try:
#        letra = next(iterador)
#        print(letra)
#    except StopIteration:
#        break

for letra in texto:
    print(letra)