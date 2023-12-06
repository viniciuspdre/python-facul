import os
os.system('cls')

soma = 0
for i in range(2):
    area = int(input('Escolha a figura que deseja calcular a área digitando seu respectivo número:\n\n1 - Triângulo\n2 - Quadrado\n3 - Retângulo\n4 - Paralelogramo\n4 - Losango\n5 -Trapézio\n6 - Círculo\n\n'))
    if area == 1:
        base = float(input('Forneça a base do triângulo: '))
        altura = float(input('Forneça a altura do triângulo: '))
        soma += base*altura/2
        print('A área do triângulo é de:',base*altura/2)
    elif area == 2:
        lado = float(input('Forneça o lado do quadrado: '))
        soma += lado*lado
        print('A área do quadrado é de:',lado*lado)
    elif area == 3:
        a = float(input('Forneça o valor do lado do paralelogramo: '))
        h = float(input('Forneça o valor da altura do paralelogramo: '))
        soma += a*h
        print('A área do paralelogramo é de:',a*h)
    elif area == 4:
        diagMaior = float(input('Forneça o valor da diagonal maior: '))
        diagMenor = float(input('Forneça o valor da diagonal menor: '))
        soma += diagMaior*diagMenor/2
        print('A área do losango é de:',diagMaior*diagMenor/2)
    elif area == 5:
        baseMaior = float(input('Forneça a base maior do trapézio: '))
        baseMenor = float(input('Forneça a base menor do trapézio: '))
        altura = float(input('Forneça a altura do trapézio: '))
        soma += (baseMaior+baseMenor)/2*altura
        print('A área do trapézio é de:',(baseMaior+baseMenor)/2*altura)
    else:
        raio = float(input('Forneça o raio do círculo: '))
        soma += raio*raio*altura
        print('A área do círculo é de:',raio*raio*altura)

print('A soma da área das duas salas é de:',soma)