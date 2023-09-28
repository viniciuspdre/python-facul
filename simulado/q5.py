import os
os.system('cls')

confirm = 1
funcionarios = []
generos = []
numeros = []
peças = []

while confirm == 1:
    funcionario = input('Digite o nome do funcionário: ')
    print('Digite o número de {0}: '.format(funcionario),end='')
    numero = int(input())
    print('Digite o gênero de {0} (0 - Masculino | 1 - Feminino): '.format(funcionario))
    genero = int(input())
    print('Digite a quantidade de peças que {0} fabrica: '.format(funcionario))
    peça = int(input())
    funcionarios.append(funcionario)
    numeros.append(numero)
    generos.append(genero)
    peças.append(peça)
    confirm = int(input('Digite 1 para continuar digitando funcionários e 2 para parar.\n'))

folhaPagamento = 0
totalPeças = 0
peçasHomem = 0; peçasMulher = 0
contHomem = 0; contMulher = 0
salarios = []
for i in range(len(funcionarios)):
    if peças[i] <= 30:
        print('O salário do funcionário',funcionarios[i],'número:',numeros[i],'é: R$ 1320.00.')
        folhaPagamento += 1320
        salarios.append(1320)
    elif peças[i] <= 35:
        print('O salário do funcionário',funcionarios[i],'número:',numeros[i],'é: R$',1320+0.03*1320*(peças[i]-30))
        folhaPagamento += 1320+0.03*1320*(peças[i]-30)
        salarios.append(1320+0.03*1320*(peças[i]-30))
    else:
        print('O salário do funcionário',funcionarios[i],'número:',numeros[i],'é: R$',1320+0.05*1320*(peças[i]-30))
        folhaPagamento += 1320+0.05*1320*(peças[i]-30)
        salarios.append(1320+0.05*1320*(peças[i]-30))
    totalPeças += peças[i]
    if generos[i] == 0:
        peçasHomem += peças[i]
        contHomem += 1
    elif generos[i] == 1:
        peçasMulher += peças[i]
        contMulher += 1

tamanho = len(salarios)
maiorSalario = 0
numeroMaiorFuncionario = 0
for j in range(tamanho-1):
    if salarios[j] > salarios[j+1]:
        maiorSalario = salarios[j]
    else:
        maiorSalario = salarios[j+1]

    
print('A folha mensal da fábrica é:',folhaPagamento)
print('O número total de peças fabricadas é:',totalPeças)
print('A média de peças fabricadas pelos homens é:',peçasHomem/contHomem)
print('A média de peças fabricadas pelas mulheres é:',peçasMulher/contMulher)
#print('O número do funcionário que recebe o maior salário é:',numeros[numeroMaiorFuncionario])