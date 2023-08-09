import os
os.system('cls')

nar = int(input('Informe quantos votos teve o Naruto: '))
sak = int(input('Informe quantos votos teve a Sakura: '))
shin= int(input('Informe quantos votos teve o Shino: '))
brancos = int(input('Informe quantos votos brancos houveram: '))
nulos = int(input('Informe quantos votos nulos houveram: '))

if(nar+sak+shin > brancos+nulos):
    print('A votação é válida.')
    if(nar>sak and nar>shin):
        print('O Naruto foi eleito')
    elif(sak>nar and sak>shin):
        print('A Sakura foi eleita')
    else:
        print('O Shino foi eleito')
else:
    print('A votação não é válida')