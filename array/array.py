import os 
os.system('cls')

numeros = [1,2,3,4,5]
valor = 0

for i in range(len(numeros)-1):
    if numeros[i] > numeros[i+1]:
        valor = numeros[i]
    else:
        valor = numeros[i+1]

print(valor)