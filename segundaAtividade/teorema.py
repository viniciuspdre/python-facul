import os
os.system('cls')

a=int(input('Forneça o valor de um lado: '))
b=int(input('Forneça o valor de um lado: '))
c=int(input('Forneça o valor de um lado: '))

if((a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==a*a+b*b)):
    print('O triângulo é retângulo!')
else:
    print('O triângulo não é retângulo!')