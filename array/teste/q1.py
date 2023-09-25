import random, os
os.system('cls')

def bubbleCres(tamanho, lista):
    troca = 1
    aux = 0
    while troca == 1:
        troca = 0
        for percorrer in range(tamanho-1):
            if lista[percorrer] > lista[percorrer+1]:
                aux = lista[percorrer+1]
                lista[percorrer+1] = lista[percorrer]
                lista[percorrer] = aux
                troca = 1
        tamanho -= 1

def bubbleDec(tamanho, lista):
    troca = 1
    aux = 0
    while troca == 1:
        troca = 0
        for percorrer in range(tamanho-1):
            if lista[percorrer] < lista[percorrer+1]:
                aux = lista[percorrer+1]
                lista[percorrer+1] = lista[percorrer]
                lista[percorrer] = aux
                troca = 1
        tamanho -= 1


numeros = []
numerosImpar = []
numerosPar = []
print('Números gerados: ',end='')

for i in range(31):
    numeros.append(random.randrange(0,100))
    print(numeros[i],'| ',end='')
    if numeros[i] % 2 == 0:
        numerosPar.append(numeros[i])
    else:
        numerosImpar.append(numeros[i])

print('\nNúmeros pares: ',end='')

for expor in range(len(numerosPar)):
    print(numerosPar[expor],'| ',end='')

print('\nNúmeros ímpares: ',end='')

for exporNovo in range(len(numerosImpar)):
    print(numerosImpar[exporNovo],'| ',end='')

tamanhoNum = len(numeros)
tamanhoPar = len(numerosPar)
tamanhoImpar = len(numerosImpar)

bubbleCres(tamanhoNum, numeros)
print('\nNúmeros gerados ordenados em ordem crescente: ',end='')

for j in range(len(numeros)):
    print(numeros[j],'| ',end='')

bubbleDec(tamanhoPar, numerosPar)
print('\nNúmeros pares em ordem decrescente: ',end='')

for j1 in range(len(numerosPar)):
    print(numerosPar[j1],'| ',end='')

somaImpar = 0

for i1 in range(len(numerosImpar)):
    if numerosImpar[i1] < 10:
        somaImpar += numerosImpar[i1]

print('\nSoma das unidades ímpares:',somaImpar)

somaPar = 0

for i2 in range(len(numerosPar)):
    if numerosPar[i2] > 9 and numerosPar[i2] < 100:
        somaPar += numerosPar[i2]

print('Soma das dezenas pares:',somaPar)

bubbleCres(tamanhoImpar, numerosImpar)
print('O produto das dezenas pares pelas unidades ímpares dividido pela soma dos maiores números pares e ímpares é:',(somaPar*somaImpar)/numerosImpar[len(numerosImpar)-1]+numerosPar[0])

print('Número central de todos os números gerados:',numeros[15])

if len(numerosPar) % 2 == 0:
    print('Números centrais dos números pares:',numerosPar[int(len(numerosPar)/2)],'e',numerosPar[int((len(numerosPar)/2)-1)])
else:
    print('Número central dos números pares:',numerosPar[int((len(numerosPar)/2))])

if len(numerosImpar) % 2 == 0:
    print('Números centrais dos números ímpares:',numerosImpar[int(len(numerosImpar)/2)],'e',numerosImpar[int((len(numerosImpar)/2)-1)])
else:
    print('Número central dos números ímpares:',numerosImpar[int((len(numerosImpar)/2))])