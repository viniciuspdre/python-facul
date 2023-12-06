import os
os.system('cls')

x = range(6)
for i in x:
    numero = int(input('Me forneça um número.'))
    if(numero < 1) and (numero > 60):
        print('O número {0} é inválido.'.format(numero))
    else:
        print('O número {0} é válido.'.format(numero))