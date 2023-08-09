import os
os.system('cls')
i = 0
numeros = []
while i < 6:
    n = int(input('Me forneça um número natural para a mega-sena: '))
    numeros.append(n)
    i=i+1

for x in numeros:
    if(x < 0):
        print('O número {0} que você escreveu é inválido.'.format(x))
    else:
        print(x)