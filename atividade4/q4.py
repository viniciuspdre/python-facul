import random,os

os.system('cls')

melodia1 = random.randint(1,10); melodia2 = random.randint(1,10); melodia3 = random.randint(1,10)
tentativa1 = random.randint(1,10); tentativa2 = random.randint(1,10); tentativa3 = random.randint(1,10)
falha = 0

while melodia1 != tentativa1 or melodia2 != tentativa2 or melodia3 != tentativa3:
    tentativa1 = random.randint(1,10); tentativa2 = random.randint(1,10); tentativa3 = random.randint(1,10)
    falha += 1
    

print('Primeira melodia mágica:',melodia1,'\nSegunda melodia mágica:',melodia2,'\nTerceira melodia mágica:',melodia3)
print('Primeira tentativa do flautista:',tentativa1,'\nSegunda tentativa do flautista:',tentativa2,'\nTerceira tentativa do flautista:',tentativa3, '\n\nNúmero de tentativas',falha)