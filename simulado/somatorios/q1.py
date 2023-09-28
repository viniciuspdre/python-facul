import os
os.system('cls')

print('S = ',end='')
numerador = 1
denominador = 1
soma = 0

for i in range(50):
    print(' + ',' ( ',numerador,' / ',denominador,' ) ',end='')
    soma += numerador/denominador
    numerador += 2
    denominador += 1

print(' = ', soma,end='')
