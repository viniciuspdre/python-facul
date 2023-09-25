import random


def valoresNegativos():
    print(random.randint(-999,-1))

rodadas = int(input('Quantos valores negativos você deseja gerar?'))

for i in range(rodadas):
    valoresNegativos()