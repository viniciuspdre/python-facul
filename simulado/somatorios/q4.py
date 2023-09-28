import os
os.system('cls')

num1 = 37
num2 = 38
den = 1
soma = 37*38

for i in range(36):
    num1 -= 1
    num2 -= 1
    den += 1
    soma += (num1*num2)/den

print(soma)