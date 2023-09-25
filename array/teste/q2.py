import os
os.system('cls')


confirmar = 1
nomes = []

while confirmar == 1:
    nome = input('Forneça o nome da pessoa: ')
    nomes.append(nome)
    confirmar = int(input('Se você não deseja informar mais nenhum nome, digite 0.\nCaso queira informar mais um nome digite 1.\n'))

troca = 1
aux = ''
tamanho = len(nomes)

while troca == 1:
    troca = 0
    for i in range(tamanho- 1):
        if nomes[i] > nomes[i+1]:
            aux = nomes[i+1]
            nomes[i+1] = nomes[i]
            nomes[i] = aux
            troca = 1
    tamanho -= 1

print('Nomes em ordem alfabética: ',end='')

for j in range(len(nomes)):
    print(nomes[j],'| ',end='')