import random

numeros = []
numerosImpares = []
numerosPares = []
maiorPar = 0
maiorImpar = 0

for i in range(31):
    numero = random.randint(1,99)
    numeros.append(numero)
    if(numero % 2 == 0):
        numerosPares.append(numero)
    else:
        numerosImpares.append(numero)


print('Todos os números: ',numeros)
print('Números pares:',numerosPares)
print('Números Ímpares:',numerosImpares)

troca  = True
aux = 0
tamanhoTotal = len(numeros)

while troca == True:
    troca = False
    for j in range(tamanhoTotal-1):
        if(numeros[j]>numeros[j+1]):
            aux = numeros[j+1]
            numeros[j+1] = numeros[j]
            numeros[j] = aux
            troca = True
    tamanhoTotal -= 1

print('Números ordenados na ordem crescente:',numeros)

for x in range(len(numeros)):
    if(numeros[x] % 2 == 0):
        maiorPar = numeros[x]
    else:
        maiorImpar = numeros[x]

tamanhoPares = len(numerosPares)
aux = 0
troca = True

while troca == True:
    troca = False
    for j in range(tamanhoPares-1):
        if(numerosPares[j]<numerosPares[j+1]):
            aux = numerosPares[j+1]
            numerosPares[j+1] = numerosPares[j]
            numerosPares[j] = aux
            troca = True
    tamanhoPares -= 1

print('Número pares ordenados na ordem descendente:',numerosPares)

somaImpar = 0

for u in range(len(numerosImpares)):
    if(numerosImpares[u] < 10):
        somaImpar += numerosImpares[u]

print('Soma dos números ímpares com uma unidade:',somaImpar)

somaPar = 0

for d in range(len(numerosPares)):
    if(numerosPares[d] > 9):
        somaPar += numerosPares[d]

print('Soma dos números pares:',somaPar)
print('Maior par:',maiorPar)
print('Maior ímpar:',maiorImpar)
print('Resultado do cálculo pedido no oitavo ponto:',(somaPar*somaImpar)/(maiorImpar+maiorPar))

print('Número central do array de números ordenado na ordem crescente:',numeros[15])

tamanhoPares = len(numerosPares)

if(tamanhoPares % 2 != 0):
    print('Número central:',numerosPares[int((tamanhoPares-1)/2)])
else:
    print('Números centrais:',numerosPares[int(tamanhoPares/2)],numerosPares[int((tamanhoPares/2)-1)])
