import os, random
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

marsh = 0
morcego = 0
tumulo = 0
valorTotal = 0
gastoDiario = []

for i in range(7):
    marsh2 = 0; morcego2 = 0; tumulo2 = 0
    valor = random.randint(0,50)
    if i == 0:
        valor = 45
    for j in range(valor):
        monstro = random.randint(1,3)
        if monstro == 1:
            marsh2 += 1
        elif monstro == 2:
            tumulo2 += 1
        else:
            morcego2 += 1 
    gastoDiario.append(marsh2*350+tumulo2*120+morcego2*50)
    valorTotal += gastoDiario[i]
    gastoDiario[i] = str(gastoDiario[i])
    marsh += marsh2
    morcego += morcego2
    tumulo += tumulo2

marsh = str(marsh)
morcego = str(morcego)
tumulo = str(tumulo)
valorTotal = str(valorTotal)


arquivo = open('atfinal/ataqueSeres.txt','w')

arquivo.write('Valor total gasto: %s\n'%valorTotal)
arquivo.write('Morcegos encontrados: %s\n'%morcego)
arquivo.write('Túmulos encontrados: %s\n'%tumulo)
arquivo.write('Bonecos encontrados: %s\n'%marsh)
for x in range(len(gastoDiario)):
    arquivo.write('Gasto diário: %s\n'%gastoDiario[x])

diaDaSemana = 0
maiorValor = '0'

for converter in range(len(gastoDiario)):
    gastoDiario[converter] = int(gastoDiario[converter])

for h in range(len(gastoDiario)):
    contador = 0
    for k in range(len(gastoDiario)):
        if gastoDiario[h] >= gastoDiario[k]:
            contador += 1
    if contador == 7:
        diaDaSemana = h

if diaDaSemana == 0:
    arquivo.write('Domingo foi o dia com maior gasto.')
elif diaDaSemana == 1:
    arquivo.write('Segunda foi o dia com maior gasto.')
elif diaDaSemana == 2:
    arquivo.write('Terça foi o dia com maior gasto.')
elif diaDaSemana == 3:
    arquivo.write('Quarta foi o dia com maior gasto.')
elif diaDaSemana == 4:
    arquivo.write('Quinta foi o dia com maior gasto.')
elif diaDaSemana == 5:
    arquivo.write('Sexta foi o dia com maior gasto.')
else:
    arquivo.write('Sábado foi o dia com maior gasto.')

arquivo.close()