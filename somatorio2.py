import os
os.system('cls')

numerador = 1
denominador = 2
contador = 0
somaNumerador = 0
somaDenominador = 0

for i in range(1,51):
    if contador <= 2:
        print(' + (', numerador, '/',denominador,end=')')
        somaNumerador += numerador
        somaDenominador += denominador
    elif contador == 3:
        print(' - (', numerador, '/',denominador,end=')')
        somaNumerador -= numerador
        somaDenominador -= denominador
    elif contador == 4:
        print(' + (', numerador, '/',denominador,end=')')
        somaNumerador += numerador
        somaDenominador += denominador
    elif contador == 5:
        print(' - (', numerador, '/',denominador,end=')')
        somaNumerador -= numerador
        somaDenominador -= denominador
    else:
        print(' + (', numerador, '/',denominador,end=')')
        somaNumerador += numerador
        somaDenominador += denominador
        contador = -1
    numerador += 1
    denominador += 2
    contador += 1
print(' =',somaNumerador,'/',somaDenominador,end='')