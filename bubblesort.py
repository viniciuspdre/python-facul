import random, os
os.system('cls')

aux = 0
numeros = []

for i in range(0,10):
    numeros.append(random.randint(0,100))

print('Números:',numeros,end='')

print('\nNúmeros ordenados: ',end='')

for j in range(len(numeros)):
    for c in range(len(numeros)-j-1):
        if(numeros[c]>numeros[c+1]):
            aux = numeros[c+1]
            numeros[c+1] = numeros[c]
            numeros[c] = aux

print(numeros)