pessoas = []
idades = []

for i in range(10):
    pessoa = input('Digite o nome da pessoa: ')
    pessoas.append(pessoa)
    print('Qual a idade de',pessoa,'?')
    idade = int(input())
    idades.append(idade)

print('Pessoas desordenadas:',pessoas)
print('Idade das pessoas:',idades)

tamanhoTotal = len(pessoas)

auxIdade = 0
auxNome = ''
troca = True

while troca == True:
    troca = False
    for j in range(tamanhoTotal-1):
        if(idades[j]>idades[j+1]):
            auxIdade = idades[j+1]
            idades[j+1] = idades[j]
            idades[j] = auxIdade
            auxNome = pessoas[j+1]
            pessoas[j+1] = pessoas[j]
            pessoas[j] = auxNome
            troca = True
    tamanhoTotal -= 1

print('Pessoas ordenadas por nome:',pessoas)
print('Idade das pessoas:',idades)

tamanhoTotal = len(idades)

while troca == True:
    troca = False
    for j in range(tamanhoTotal-1):
        if(idades[j]>idades[j+1]):
            auxIdade = idades[j+1]
            idades[j+1] = idades[j]
            idades[j] = auxIdade
            auxNome = pessoas[j+1]
            pessoas[j+1] = pessoas[j]
            pessoas[j] = auxNome
            troca = True
    tamanhoTotal -= 1

print('Pessoas ordenadas por idade:',pessoas)
print('Idade das pessoas:',idades)