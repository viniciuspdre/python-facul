import random, os
os.system('cls')

palpite = []
noRepeat = [0]

for i in range(6):
    valor = random.randint(1,60)
    palpite.append(valor)
    for j in range(len(noRepeat)):
        if palpite[i] == noRepeat[j]:
            valor = random.randint(1,60)
            palpite[i] = valor
    noRepeat.append(palpite[i])

print(palpite)

print('Palpite ordenado: ',end='')

for j in range(len(palpite)):
    if palpite[j] < 10:
        print('0'+str(palpite[j]),'| ',end='')
    else:
        print(palpite[j],'| ',end='')