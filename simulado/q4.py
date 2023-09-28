import os
os.system('cls')

def fatorial(valor):
    produto = 1
    while valor > 1:
        produto *= valor
        valor -= 1
    return produto

n = int(input('Quantos termos você deseja exibir e calcular?\n'))

print('\nS = ',end='')
numerador = 2
denominador = -3
soma = 0

for i in range(n):
    print(' +','(',numerador,'! /',denominador,') ', end='')
    soma += fatorial(numerador)/denominador
    numerador += 4
    denominador -= 4

print('=',soma)