import os

os.system('cls')
tipoPoder = False

port = float(input('Forneça sua nota em português: '))
mat = float(input('Forneça sua nota em matemática: '))
poder = int(input('Forneça o valor que você recebeu para o poder: '))
tipoPoder = bool(input('Se você for telepata digite 1, se não for, digite 0.'))

if (port < 8 and mat < 7):
    os.system('cls')
    print('Você foi reprovado tanto em português, quanto em matemática.')
    
elif (mat < 7):
    os.system('cls') 
    print('Você foi reprovado em matemática.')
elif (port < 8):
    os.system('cls')
    print('Você foi reprovado em português.')
else:
    os.system('cls')
    if(poder == 10):
        print('ÔMEGA')
    elif(tipoPoder == True):
        media = (port+mat+2*poder)/4
        print('Sua média foi: {0}'.format(media))
    elif(tipoPoder == False):
        media = (port+mat+poder)/3
        print('Sua média foi: {0}'.format(media))