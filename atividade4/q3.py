import random,os

os.system('cls')
queijoTotal = 0

for i in range(1, 6):
    ligeiro = random.randint(0,1)
    print('Dia', i)
    if(ligeiro == 0):
        print('Ele começou com o pé esquerdo. Vamos tentar novamente no próximo dia...')
        print('-----------------------------------------------------------------------')
    else:
        queijos = random.randint(0,30)
        print('Retirou ',queijos,'queijos.')
        print('-----------------------------------------------------------------------')
        queijoTotal += queijos

print('Ele retirou no total: ', queijoTotal,'queijos.')