import os, random
os.system('cls')

def bolha(lista):
    troca = True
    tam = len(lista)
    while troca == True and tam > 0:
        troca = False
        for i in range(tam-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                troca = True
        tam -= 1
    return lista

vetor = []
somaPares = 0
divPares = 0
somaImpares = 0
divImpares = 0

for i in range(20):
    vetor.append(random.randint(1,200))
    if vetor[i] % 2 == 0:
        somaPares += vetor[i]
        divPares += 1
    else:
        somaImpares += vetor[i]*i
        divImpares += i

print('A média dos números pares é:',somaPares/divPares)
print('A média ponderada dos números ímpares é:',somaImpares/divImpares)
print('Array ordenado: ',end='')
vetor = bolha(vetor)

for j in range(len(vetor)):
    print(vetor[j],end=' | ')