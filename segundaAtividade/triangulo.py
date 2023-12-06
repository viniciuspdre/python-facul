import os
os.system('cls')

a = int(input('Me forneça o primeiro lado do triângulo: '))
b = int(input('Me forneça o segundo lado do triângulo: '))
c = int(input('Me forneça o terceiro lado do triângulo: '))

if(a>b+c or b>a+c or c>b+a):
    print('Não é um triângulo.')
else:
    print('É um triângulo.')
    if(a==b and a==c):
        print('O triângulo é equilátero.')
    elif(a==b or a==c or b==c):
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')