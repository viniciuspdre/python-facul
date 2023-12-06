import os, random
os.system('cls')

def gerarNumero(lista):
    numero = random.randint(1,9)
    contador = 0
    i = 0
    while contador != len(lista):
        while i < len(lista):
            if numero != lista[i]:
                contador += 1
            else:
                contador = 0
                numero = random.randint(1,9)
            i += 1
            if contador == 0:
                i = 0
    lista.append(numero)

senha = [random.randint(1,9)]
for gerar in range(3):
    gerarNumero(senha)

print(senha)

cPreto = 0
cBranco = 0

c = 0
while c < 10:
    tentativa = []
    for perguntar in range(4):
        numero = int(input('Digite um numero:'))
        tentativa.append(numero)
    for i in range(len(senha)):
        for j in range(len(tentativa)):
            if senha[i] == tentativa[j]:
                if i == j:
                    cPreto += 1
                else:
                    cBranco += 1
    if cPreto == 4:
        print('Parabéns! Você descobriu a senha!')
        c = 10
    elif cPreto == 3:
        print('Três pretos.')
    elif cPreto == 2:
        print('Dois pretos.')
    elif cPreto == 1 and cBranco == 2:
        print('Um preto e dois brancos.')
    elif cPreto == 1:
        print('Um preto.')
    elif cbranco == 3:
        print('Três brancos.')
    elif cBranco == 2:
        print('Dois brancos.')
    elif cBranco == 1:
        print('Um branco.')
    cPreto = 0
    cbranco = 0
    c += 1