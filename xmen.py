import os

os.system('cls')
tipoPoder = 0

port = float(input('Forneça sua nota em português: '))
if(port<8):
    print('Você reprovou em português.')
else:
    mat = float(input('Forneça sua nota em matemática: '))
    if(mat<7):
        print('Você não passou em matemática.')
    else:
        poder = int(input('Forneça o valor que você recebeu para o poder: '))
        tipoPoder = int(input('Se você for telepata digite 1, se não for, digite 0.\n'))
        if(poder == 10):
            print('Ômega.')
        elif(tipoPoder == 1):
            print('Sua média foi: {0}'.format((port+mat+poder*2)/4))
        elif(tipoPoder == 0):
            print('Sua média foi: {0}'.format((port+mat+poder)/3))
        else:
            print('[ERRO]Informe um valor válido para o tipo do poder!')