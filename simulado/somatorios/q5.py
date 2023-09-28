import os
os.system('cls')

sinal = 0
contador = 3
num = 1
den = 1
soma = 0

for i in range(10):
    if sinal == 0:
        soma += num/den
        sinal += 1
    else:
        soma -= num/den
        sinal = 0
    num += 1
    den += contador
    contador += 2

print(soma)