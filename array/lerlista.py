import os
os.system('cls')

numeros = []
qtd = int(input('Quantos números você deseja fornecer?\n'))

for i in range(qtd):
    numero = float(input('Forneça um número: '))
    numeros.append(numero)

print(numeros)
