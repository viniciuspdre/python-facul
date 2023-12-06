import os, random
os.system('cls')

primeiroNum = []
segundoNum = []
terceiroNum = []

for i in range(10):
    primeiroNum.append(random.randint(1,100))
    segundoNum.append(random.randint(1,100))
    terceiroNum.append(random.randint(1,100))
    if terceiroNum[i]*terceiroNum[i] == segundoNum[i]*segundoNum[i] + primeiroNum[i]*primeiroNum[i] or primeiroNum[i]*primeiroNum[i] == segundoNum[i]*segundoNum[i] + terceiroNum[i]*terceiroNum[i] or segundoNum[i]*segundoNum[i] == primeiroNum[i]*primeiroNum[i] + terceiroNum[i]*terceiroNum[i]:
        print('O trio de números:',primeiroNum[i],' |',segundoNum[i],' |',terceiroNum[i],' | forma um triângulo retângulo.')
    else:
        print('O trio de números:',primeiroNum[i],' |',segundoNum[i],' |',terceiroNum[i],' | não forma um triângulo retângulo.')