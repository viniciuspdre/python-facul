import os 
os.system('cls')

num = 1000
den = 1
sinal = 0
soma = 0

for i in range(50):
    if sinal == 0:
        soma += num/den
        sinal += 1
    else:
        soma -= num/den
        sinal = 0
    num -= 3
    den += 1

print(soma)