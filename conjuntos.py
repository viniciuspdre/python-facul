import random, os
os.system('cls')

def remover(vetor, indice):
    novoVetor = []
    for i in range(len(vetor)):
        if i != indice:
            novoVetor.append(vetor[i])
    vetor = novoVetor
    novoVetor = []

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
    if len(novoVetor) > 0:
        vetorIntersec = novoVetor
    return imprimirVetor(vetorIntersec)
    
def uniao(vetor1,vetor2):
    vetorUniao = vetor1
    novoVetor = []
    for i in range(len(vetor2)):
        vetorUniao.append(vetor2[i])
    vetorUniao = bolha(vetorUniao)
    for j in range(len(vetorUniao)-1):
        if vetorUniao[j] != vetorUniao[j+1]:
            novoVetor.append(vetorUniao[j])
    novoVetor = bolha(novoVetor)
    if vetorUniao[len(vetorUniao)-1] != novoVetor[len(novoVetor)-1]:
        novoVetor.append(novoVetor[len(novoVetor)-1])
    vetorUniao = novoVetor
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
#     imprimirVetor(vetorSubtracao)

def diferenca(vetor1, vetor2):
    for i in range(len(vetor1)):
        for j in range(len(vetor2)):
            if vetor1[i] == vetor2[j]:
                vetor1 = remover(vetor1,i)
                break
    return imprimirVetor(vetor1)

a = []
b = []

for vetorA in range(random.randint(1,10)):
    a.append(random.randint(10,99))

for vetorB in range(random.randint(1,10)):
    b.append(random.randint(10,99))

#imprimir os vetores a e b
a = bolha(a)
b = bolha(b)
print('--------------- Vetor A ---------------')
imprimirVetor(a)
print('--------------- Vetor B ---------------')
imprimirVetor(b)
print('--------------- Intersecção ---------------')
intersec(a,b)
print('--------------- União ---------------')
uniao(a,b)
print('--------------- Diferença ---------------')
diferenca(a,b)
# subtracao(a,b)