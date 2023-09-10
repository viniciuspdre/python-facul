import os
os.system('cls')

numeros = [1,2,3,4,5]
aux = 1

for i in range(len(numeros)-1):
    if numeros[i+1] > numeros[i]:
        aux += 1

if aux == len(numeros):
    print('Está em ordem crescente.')
else:
    print('Está desordenado')