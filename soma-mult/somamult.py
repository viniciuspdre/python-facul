import os 
os.system('cls')

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if(num2 % 2 == 0):
    print('O número {0} é par.\n'.format(num2))
    print('A soma do número 1 mais o número 2 é: ', num1+num2)
else:
    print('O número {0} é impar.\n'.format(num2))
    print('A multiplicação do número 1 com o número 2 é: ', num1*num2)