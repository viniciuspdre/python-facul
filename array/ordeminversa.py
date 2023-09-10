import random, os
os.system('cls')


numeros = []

for c in range(10):
    numeros.append(random.randrange(0,20))

print(numeros)

i = 0
fim = len(numeros)
while i < fim:
    for j in range(len(numeros)-i-1):
        numeros[j+1], numeros[j] = numeros[j], numeros[j+1]
    i += 1
    fim -= 1

print(numeros)