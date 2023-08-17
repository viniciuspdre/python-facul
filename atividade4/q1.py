import random,os

os.system('cls')

osWinchester = 0; ghostBusters = 0; vanHelsing = 0

for i in range(45):
    botaoPressionado = random.randint(1,3)
    if(botaoPressionado == 1):
        osWinchester += 1
    elif(botaoPressionado == 2):
        ghostBusters += 1
    else:
        vanHelsing +=1

print('Quantidade de vezes que o botão foi apertado para:\nIrmãos Winchester:',osWinchester,'\nGhostBusters:',ghostBusters,'\nVan Helsing: ',vanHelsing,'\nO valor gasto em reais foi de: ', osWinchester*120+ghostBusters*350+vanHelsing*50)