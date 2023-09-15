import os
os.system('cls')

nomes = []
idades = []

c = 'Sim'

while c.lower() == 'sim':
    nome = input('Me forença o nome da pessoa: ')
    print('Me forneça a idade de {0}'.format(nome))
    idade = int(input())
    nomes.append(nome)
    idades.append(idade)
    c = input('Digite sim se você deseja continuar no programa: ')

print(nomes,idades)

qtd = len(nomes)
troca = True
while troca == True:
    troca = False
    for i in range(qtd - 1):
        if idades[i] > idades[i+1]:
            idades[i], idades[i+1] = idades[i+1], idades[i]
            nomes[i], nomes[i+1] = nomes[i+1], nomes[i]
            troca = True
    qtd -= 1 #qtd = qtd - 1

print(nomes,idades)