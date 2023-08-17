import os

os.system('cls')

num1 = int(input('Me forneça um número: '))
num2 = int(input('Me forneça um número: '))

if(num1 % 2 == 0 and num2 % 2 == 0):
    print('A soma desses números é: ', num1+num2)
elif(num1 % 2 != 0 and num2 % 2 != 0):
    print('A subtração do primeiro número com o segundo é: ', num1-num2)
else:
    print('A multiplicação desses números é: ', num1*num2)