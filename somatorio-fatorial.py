import os
os.system('cls')

def fatorial(numero):
    i = 1 # 2 3 4 5 6
    res = 1 # 1 2 6 24 120
    while i <= numero:
        res = res * i # res *= i
        i+=1
    return res

resultado = 0
numerador = 2
denominador = -3
print('S = ',end='')
for i in range(3):
    print(' + (',numerador,'!','/',denominador,')',end='')
    resultado = resultado + fatorial(numerador)/denominador
    numerador += 4
    denominador -= 4 #denominador = denominador - 4

print(' =',resultado,end='')