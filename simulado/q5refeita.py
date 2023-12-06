import os
os.system('cls')

numeroOperarios = []
sexoOperarios = []
pecasOperarios = []
salarioOperarios = []
pecasHomens = []
pecasMulheres = []

numero = 1
while numero != 0:
    numero = int(input('Digite o número do operário: '))
    pecas = int(input('Digite quantas peças o operário fabrica no mês: '))
    sexo = int(input('Digite o sexo do operário (0 - Masculino | 1 - Feminino): '))
    numeroOperarios.append(numero)
    pecasOperarios.append(pecas)
    if sexo == 0:
        pecasHomens.append(pecas)
    elif sexo == 1:
        pecasMulheres.append(pecas)
    while sexo != 0 and sexo != 1:
        sexo = int(input('[VALOR ANTERIOR INVÁLIDO]Digite o sexo do operário (0 - Masculino | 1 - Feminino): '))
        if sexo == 0:
            pecasHomens.append(pecas)
        elif sexo == 1:
            pecasMulheres.append(pecas)
    sexoOperarios.append(sexo)
    if pecas <= 30:
        salarioOperarios.append(1300)
    elif pecas <= 35:
        salarioOperarios.append(1300+0.03*1300*(pecas-30))
    else:
        salarioOperarios.append(1300+0.05*1300*(pecas-30))
    
folhaPagamento = 0
totalPecas = 0
totalPecasHomens = 0
totalPecasMulheres = 0

for i in range(len(numeroOperarios)):
    print('| O salário do operário de número',numeroOperarios[i],'é',salarioOperarios[i],'|')
    folhaPagamento += salarioOperarios[i]
    totalPecas += pecasOperarios[i]

for homem in range(len(pecasHomens)):
    totalPecasHomens += pecasHomens[homem]

for mulher in range(len(pecasMulheres)):
    totalPecasMulheres += pecasMulheres[mulher]

print('O total da folha mensal da empresa é:', folhaPagamento)
print('O número total de peças fabricadas por mês é:', totalPecas)
print('A média de peças fabricadas por homens é:',totalPecasHomens/len(pecasHomens))
print('A média de peças fabricadas por mulheres é:',totalPecasMulheres/len(pecasMulheres))

fim = len(numeroOperarios)
troca = True

while troca and fim > 0:
    troca = False
    for j in range(fim - 1):
        if salarioOperarios[j] > salarioOperarios[j+1]:
            aux = salarioOperarios[j]
            salarioOperarios[j] = salarioOperarios[j+1]
            salarioOperarios[j+1] = aux
            aux = numeroOperarios[j]
            numeroOperarios[j] = numeroOperarios[j+1]
            numeroOperarios[j+1] = aux
            troca = True
    fim -= 1

print('O operário com o maior salário é o operário de número:',numeroOperarios[len(numeroOperarios)-1])