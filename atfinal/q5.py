import os
os.system('cls')


arquivo = open('atfinal\q5_dados.txt','r')
homem = 0
mulher = 0
casado = 0
maisFilho = 0
nomes = []
idades = []
for linha in arquivo.readlines():
    virgulaSexo = 0
    virgulaCasado = 0
    virgulaFilho = 0
    idade = ''
    nome = ''
    for i in range(len(linha)):
        if virgulaSexo == 2:
            if linha[i+1] == '1':
                homem += 1
            elif linha[i+1] == '2':
                mulher += 1
        elif virgulaCasado == 5:
            virgulaCasado += 1
            if linha[i+1] == 'c':
                casado += 1
        elif virgulaFilho == 4:
            virgulaFilho += 1
            if int(linha[i+1]) > 1:
                maisFilho += 1
        elif virgulaSexo == 0:
            idade += linha[i]
        elif virgulaSexo == 6:
            if linha[i] != ' ':
                nome += linha[i]
        if linha[i] == ',':
            virgulaSexo += 1
            virgulaCasado += 1
            virgulaFilho += 1
    novaIdade = ''
    for x in range(len(idade)-1):
        novaIdade += idade[x]
    idade = novaIdade
    nomes.append(nome)
    idades.append(int(idade))

trocou = True
tam = len(nomes)
while trocou == True and tam > 0:
    trocou = False
    for j in range(tam-1):
        if idades[j] > idades[j+1]:
            aux = idades[j+1]
            idades[j+1] = idades[j]
            idades[j] = aux
            auxNome = nomes[j+1]
            nomes[j+1] = nomes[j]
            nomes[j] = auxNome

print('Quantidade de homens:',homem)
print('Quantidade de mulheres:',mulher)
print('Quantidade de pessoas casadas:',casado)
print('Quantidade de pessoas com mais de um filho:',maisFilho)
print('Nome da pessoa mais velha e idade:',nomes[len(nomes)-1],idades[len(idades)-1])
arquivo.close()