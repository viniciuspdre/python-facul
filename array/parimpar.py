import random,os 
os.system('cls')


numeros = []
par = []
impar = []

for i in range(20):
    numero = random.randint(0,10)
    if(numero%2==0):
        par.append(numero)
    else:
        impar.append(numero)
    numeros.append(numero)

print(numeros,par,impar)