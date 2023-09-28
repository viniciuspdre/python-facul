import os
os.system('cls')
#Leia o nome de N pessoas
#Exiba em ordem crescente

def bolha(lista,tamanho):
    tamanho=len(lista)

    trocou=True

    while trocou==True:
        trocou=False
        for i in range(tamanho-1): 
            if lista[i]>lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
        tamanho=tamanho-1

nome=[]

conf=1

while conf==1:
    names=(input('Qual o nome da pessoa: '))
    nome.append(names)
    conf=int(input('Quer continuar? 1 = Sim | 0 = Não'))
tamanho=len(nome)
print('Você digitou:',tamanho,'nomes.')

print('Você inseriu os nomes: ',end='')

for i in range(tamanho):
    print(' | ',end='')
    print(nome[i],end='')

bolha(nome,tamanho)

print('\n Ordenado:',end='')
for k in range(len(nome)):
    print(' | ',end='')
    print(nome[k],end='')
