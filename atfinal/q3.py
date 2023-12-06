import os
os.system('cls')


for i in range(2):
    print('Olá, João, gostaria de saber qual bola você comprou.\n\nDigite 1 se foi bola de futebol;\nDigite 2 se foi bola de vôlei;\nDigite 3 se foi bola de boliche;\nDigite 4 se foi bola de basquete;\nDigite 5 se foi bola de gude.\n')
    tipo = int(input())
    peso = int(input('Agora me forneça o peso da bola em gramas: '))
    if tipo == 1:
        if peso >= 410 and peso <= 450:
            print('A bola é oficial.')
        else:
            print('A bola não é oficial.')
    elif tipo == 2:
        if peso >= 185 and peso <= 240:
            print('A bola é oficial.')
        else:
            print('A bola não é oficial.')
    elif tipo == 3:
        if peso >= 800 and peso <= 1200:
            print('A bola é oficial.')
        else:
            print('A bola não é oficial.')
    elif tipo == 4:
        if peso >= 450 and peso <= 600:
            print('A bola é oficial.')
        else:
            print('A bola não é oficial.')
    else:
        if peso >= 5 and peso <= 15:
            print('A bola é oficial.')
        else:
            print('A bola não é oficial.')
    continuar = input('Digite enter para continuar...')
    os.system('cls')