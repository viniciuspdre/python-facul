import random

palpite = []
auxValor = 0

for i in range(6):
    valor = random.randint(1,60)
    while valor == auxValor:
        valor = random.randint(1,60)
    palpite.append(valor)
    auxValor = valor

tam = len(palpite)

troca = True
aux = 0

while troca == True:
    troca = False
    for j in range(tam-1):
        if(palpite[j]>palpite[j+1]):
            aux = palpite[j+1]
            palpite[j+1] = palpite[j]
            palpite[j] = aux
            troca = True
        # if(palpite[j]==palpite[j+1]):
        #     valor = random.randint
        #     palpite[j] = valor
    tam -= 1

print('Seu palpite ordenado com as unidades consertadas: ',end='')

for j in range(len(palpite)):
    if(palpite[j] < 10):
        print('0',palpite[j], end=' ')
    else:
        print(palpite[j],end=' ')
        
