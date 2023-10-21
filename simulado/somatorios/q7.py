import os
os.system('cls')

num = 480
den = 10
soma = 0
sinal = 0

for i in range(30):
    if sinal == 0:
        soma += num/den
        sinal += 1
    else:
        soma -= num/den
        sinal = 0
    num -= 5
    den += 1
    
print(soma)