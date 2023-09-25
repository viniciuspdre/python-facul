import os
os.system('cls')


def calculoMedia(notaPortugues, notaMat, notaPoder, tipoPoder):
    if tipoPoder == 1:
        print('Sua média é:', (notaPoder * 2 + notaMat + notaPortugues)/4)
    else:
        print('Sua média é:', (notaPoder + notaMat + notaPortugues)/3)

def provaPoder():
    global notaPoder
    global tipoPoder
    notaPoder = int(input('Qual valor você recebeu para o poder?\nInsira um valor de 0 a 10: '))
    if notaPoder == 10:
        os.system('cls')
        print('//.......................................................................\n//....ÔÔÔÔÔÔÔ....ÔMMMMM...MMMMMM.EEEEEEEEEEE....GGGGGGG.......AAAAA......\n//...ÔÔÔÔÔÔÔÔÔÔ..ÔMMMMM...MMMMMM.EEEEEEEEEEE..GGGGGGGGGG......AAAAA......\n//..ÔÔÔÔÔÔÔÔÔÔÔÔ.ÔMMMMM...MMMMMM.EEEEEEEEEEE.GGGGGGGGGGGG....AAAAAA......\n//..ÔÔÔÔÔ..ÔÔÔÔÔ.ÔMMMMMM.MMMMMMM.EEEE........GGGGG..GGGGG....AAAAAAA.....\n//.ÔÔÔÔÔ....ÔÔÔÔÔÔMMMMMM.MMMMMMM.EEEE.......EGGGG....GGG....AAAAAAAA.....\n//.ÔÔÔÔ......ÔÔÔÔÔMMMMMM.MMMMMMM.EEEEEEEEEE.EGGG............AAAAAAAA.....\n//.ÔÔÔÔ......ÔÔÔÔÔMMMMMMMMMMMMMM.EEEEEEEEEE.EGGG..GGGGGGGG..AAAA.AAAA....\n//.ÔÔÔÔ......ÔÔÔÔÔMMMMMMMMMMMMMM.EEEEEEEEEE.EGGG..GGGGGGGG.AAAAAAAAAA....\n//.ÔÔÔÔÔ....ÔÔÔÔÔÔMMMMMMMMMMMMMM.EEEE.......EGGGG.GGGGGGGG.AAAAAAAAAAA...\n//..ÔÔÔÔÔ..ÔÔÔÔÔ.ÔMMM.MMMMM.MMMM.EEEE........GGGGG....GGGG.AAAAAAAAAAA...\n//..ÔÔÔÔÔÔÔÔÔÔÔÔ.ÔMMM.MMMMM.MMMM.EEEEEEEEEEE.GGGGGGGGGGGG.GAAA....AAAA...\n//...ÔÔÔÔÔÔÔÔÔÔ..ÔMMM.MMMMM.MMMM.EEEEEEEEEEE..GGGGGGGGGG..GAAA.....AAAA..\n//.....ÔÔÔÔÔÔ....ÔMMM.MMMMM.MMMM.EEEEEEEEEEE....GGGGGGG..GGAAA.....AAAA..\n//.......................................................................')
    else:
        tipoPoder = int(input('Caso você seja um telepata digite 1, se não for, digite qualquer outro valor numérico.\n'))
        calculoMedia(notaPortugues, notaMat, notaPoder, tipoPoder)

def provaMat():
    global notaMat
    notaMat = float(input('Qual sua nota em matemática?\n'))
    if notaMat >= 7:
        provaPoder()
    else:
        print('Você foi eliminado na segunda fase.')

def provaPort():
    global notaPortugues
    notaPortugues = float(input('Qual a sua nota na prova de português?\n'))
    if notaPortugues >= 8:
        provaMat()
    else:
        print('Você foi eliminado na primeira fase.')
    
provaPort()