import os

valor = int(input('Digite um valor: '))
os.system('cls')

if(valor%2 == 0 and valor%3 == 0):
    print('O número é múltiplo de 2 e 3 ao mesmo tempo!')
else:
    print('O número não é múltilpo de 2 e 3 ao mesmo tempo!')