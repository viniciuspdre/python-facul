import random, os
os.system('cls')

def valoresReais():
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    print(x/y)

rodadas = int(input('Quantos valores negativos você deseja gerar?\n'))

for i in range(rodadas):
    valoresReais()