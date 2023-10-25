import random, os
os.system('cls')

def bolha(vetor):
    tam = len(vetor)
    troca = True
    while troca and tam > 0:
        troca = False
        for i in range(tam-1):
            if vetor[i] > vetor[i+1]:
                aux = vetor[i+1]
                vetor[i+1] = vetor[i]
                vetor[i] = aux
                troca = True
        tam -= 1
    return vetor

def imprimirVetor(vetor):
    print('Vetor impresso: ',end='')
    if len(vetor) == 0:
        print('Não há elementos.')
    else:
        for i in range(len(vetor)):
            print(vetor[i],end=' | ')
    print('\n')

def maiorVetor(vetor1, vetor2):
    if len(vetor1) > len(vetor2):
        return 1
    else:
        return 2

def intersec(vetor1, vetor2):
    validacao = maiorVetor(vetor1, vetor2)
    vetorIntersec = []
    if validacao == 1:
        for i in range(len(vetor1)):
            for j in range(len(vetor2)):
                if vetor1[i] == vetor2[j]:
                    vetorIntersec.append(vetor1[i])
    else:
        for i in range(len(vetor2)):
            for j in range(len(vetor1)):
                if vetor2[i] == vetor1[j]:
                    vetorIntersec.append(vetor2[i])
    novoVetor = []
    tam = len(vetorIntersec)
    vetorIntersec = bolha(vetorIntersec)
    for j in range(tam-1):
        if vetorIntersec[j] != vetorIntersec[j+1]:
            novoVetor.append(vetorIntersec[j])
    if tam > 1:
        novoVetor.append(vetorIntersec[tam-1])
    if len(novoVetor) > 0:
        vetorIntersec = novoVetor
    return imprimirVetor(vetorIntersec)
    
def uniao(vetor1,vetor2):
    vetorTemp = []
    vetorUniao = vetor1
    vetorUniao += vetor2
    bolha(vetorUniao)
    for i in range(len(vetorUniao)-1):
        if vetorUniao[i] != vetorUniao[i+1]:
            vetorTemp.append(vetorUniao[i])
    vetorTemp.append(vetorUniao[len(vetorUniao)-1])
    vetorUniao = vetorTemp
    return imprimirVetor(vetorUniao)

# def subtracao(vetor1,vetor2):
#     validacao = maiorVetor(vetor1,vetor2)
#     vetorSubtracao = []
#     if validacao == 1:
#         tam = vetor2
#         for i in range(len(vetor1)):
#             if i > tam - 1:
#                 vetor2.append(0)
#     else:
#         tam = vetor1
#         for i in range(len(vetor2)):
#             if i > tam - 1:
#                 vetor1.append(0)
#     return imprimirVetor(vetorSubtracao)

def diferenca(vetor1, vetor2):
    vetorDiferenca = []
    for i in range(len(vetor1)):
        contador = 0
        for j in range(len(vetor2)):
            if vetor1[i] != vetor2[j]:
                contador += 1
                if contador == len(vetor2):
                    vetorDiferenca.append(vetor1[i])
        contador = 0
    return imprimirVetor(vetorDiferenca)

def contido(vetor1, vetor2):
    if len(vetor1) == len(vetor2):
        contador = 0
        for i in range(len(vetor1)):
            if vetor1[i] == vetor2[i]:
                contador += 1
        if contador == len(vetor1):
            return 'Os vetores são iguais.'
    elif len(vetor1) > len(vetor2):
        contador = 0
        for i in range(len(vetor2)):
            for j in range(len(vetor1)):
                if vetor2[i] == vetor1[j]:
                    contador += 1
        if contador == len(vetor2):
            return 'O vetor B está contido no vetor A'
        return 'Nenhum vetor está contido no outro'
    elif len(vetor2) > len(vetor1):
        contador = 0
        for i in range(len(vetor1)):
            for j in range(len(vetor2)):
                if vetor1[i] == vetor2[j]:
                    contador += 1
        if contador == len(vetor1):
            return 'O vetor A está contido no vetor B'
        return 'Nenhum vetor está contido no outro'
    return 'Nenhum vetor está contido no outro.'
    
a = [random.randint(10,99)]
b = [random.randint(10,99)]

for vetorA in range(random.randint(0,9)):
    valor = random.randint(10,99)
    for i in range(len(a)):
        while valor == a[i]:
            valor = random.randint(10,99)
    a.append(valor)

for vetorB in range(random.randint(0,9)):
    valor = random.randint(10,99)
    for i in range(len(b)):
        while valor == b[i]:
            valor = random.randint(10,99)
    b.append(valor)

#imprimir os vetores a e b
a = bolha(a)
b = bolha(b)
print('--------------- Vetor A ---------------')
imprimirVetor(a)
print('--------------- Vetor B ---------------')
imprimirVetor(b)
print('--------------- Intersecção (A ∩ B) ---------------')
intersec(a,b)
print('--------------- União (A ∪ B) ---------------')
uniao(a,b)
print('--------------- Diferença (A - B) ---------------')
diferenca(a,b)
print('--------------- Contidos ---------------')
checagemContido = contido(a,b)
print(checagemContido)