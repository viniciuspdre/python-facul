import random,os
os.system('cls')

paisesAtingidos = 0

for i in range(195):
    disparo = random.randint(1,500)
    if(disparo % 11 == 0 and disparo > 11 and disparo < 300):
        paisesAtingidos += 1
    
print('Foram atingidos um total de:',paisesAtingidos,'países.')