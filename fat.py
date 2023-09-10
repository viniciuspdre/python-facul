import os
os.system('cls')

fat = int(input('Forneça um número para calcular o fatorial: '))
i = 1
res = 1

while i != fat:
    print(fat, 'x ',end='')
    res *= fat
    fat -= 1

print(i , '=',res,end='')