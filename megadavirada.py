import os, random
os.system('cls')

numeros  = [random.randint(1,9)]

for i in range(8):
    valor = random.randint(1,9)
    for j in range(len(numeros)):
        if valor == numeros[j]:
            valorAnterior = valor
            valor = random.randint(1,9)
            while valor == valorAnterior:
                valor = random.randint(1,9)
    numeros.append(valor)

print(numeros)