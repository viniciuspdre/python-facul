import os
os.system('cls')

def bolha(list):
    length = len(list)
    switch = True
    while switch and length > 0:
        switch = False
        for i in range(length-1):
            if list[i] > list[i+1]:
                switch = True
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
        length -= 1
    return list


arquivo = open('atfinal\original.txt','r')
nomes = []
for linha in arquivo.readlines():
    nomes.append(linha)

bolha(nomes)

arquivo = open('atfinal\original.txt','w')
for i in range(len(nomes)):
    arquivo.write(nomes[i])

arquivo.close()