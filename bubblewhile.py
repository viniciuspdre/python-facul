import os, random
os.system('cls')

numeros = []

for i in range(10):
    numeros.append(random.randint(0,100))
print(numeros)

fim = len(numeros)
aux = 1

while aux == 1:
    aux = 0
    for j in range(fim - 1):
        if(numeros[j]>numeros[j+1]):
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
            aux = 1
    fim = fim - 1

print(numeros)