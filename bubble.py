import random, os
os.system('cls')


numeros = []
print('Números: ',end='')

for i in range(0,100):
    numero = random.randint(1,100)
    numeros.append(numero)
    print(numeros[i],end=', ')

valor = 0
indice = 0
for x in range(0, len(numeros)):
    if numeros[x] > valor:
        valor = numeros[x]
        indice = x

print('\nMaior valor da lista: {0}\níndice desse valor na lista: {1}'.format(valor,indice))

#ordenacao da lista

valores1 = 0
valores2 = 0
for c in range(0, len(numeros)):
    for c1 in range(0, len(numeros)-c-1):
        valores1 = numeros[c1]
        for c2 in range(1, len(numeros)-c):
            valores2 = numeros[c2]
        if valores1 > valores2:
            numeros[c1] = valores2
            numeros[c2] = valores1
        

print(numeros)