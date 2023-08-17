import os

os.system('cls')

n = 2
c = 0
soma = 0

for i in range(50):
    if(c == 0):
        soma += n
        c += 1
    else:
        soma -= n
        c = 0
    n += 2

print('A soma dos primeiros 50 termos da sequência passada foi:', soma)