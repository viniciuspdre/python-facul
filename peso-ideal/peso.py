import os
os.system('cls')

sexo = input('Se você for do sexo masculino digite M, se for feminino digite F.\n')
altura = float(input('Digite sua altura: '))

if(sexo.lower() == 'm'):
    print('O seu peso ideal é: ', (72.2*altura)-58)
elif(sexo.lower() == 'f'):
    print('O seu peso ideal é: ', (62.1*altura)-44.7)
else:
    print('Forneça um valor válido para o sexo!')