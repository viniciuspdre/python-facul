import os
os.system('cls')

def tipoTriangulo(a,b,c):
    if a==b==c:
        print('É um triângulo equilátero.')
    elif (a==b and a != c) or (b==c and b != a) or (c==a and c!= b):
        print('É um triângulo isósceles.')
    else:
        print('É um triângulo escaleno.')

def testeTriangulo(a,b,c): 
    if a > b+c or b > a+c or c > a+b:
        print('Não é um triângulo.')
    else:
        print('É um triângulo.')
        tipoTriangulo(a,b,c)

testeTriangulo(4,5,6)