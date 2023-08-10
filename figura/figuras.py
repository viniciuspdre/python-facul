import math
import os
os.system('cls')

confirm = ''
print('Escreva sem acentuação.')
while confirm.lower() != 'sim':
    area = input('Você deseja calcular a área de qual figura?')
    os.system('cls')
    if area.lower() == 'triangulo':
        b = int(input('Forneça o valor da base: '))
        h = int(input('Forneça o valor da altura: '))
        res = (b*h)/2
        print('O resultado da área do triângulo é: '+ str(res))
    elif area.lower() == 'quadrado':
        l = int(input('Forneça o lado do quadrado: '))
        res = l*l
        print('O resultado da área do quadrado é: '+ str(res))
    elif area.lower() == 'circulo':
        quest = input('Você deseja fornecer o raio ou o diâmetro?')
        if quest.lower() == 'raio':
            r = int(input('Forneça o valor do raio: '))
            res = r*r*math.pi
            print('O resultado da área do círculo é: '+ str(res))
        elif quest.lower() == 'diametro':
            d = int(input('Forneça o valor do diâmetro: '))
            r = d/2
            res = r*r*math.pi
            print('O resultado da área do círculo é: '+ str(res))
    confirm = input('Você deseja sair do programa? ')
    os.system('cls')