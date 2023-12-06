import os, random
os.system('cls')


arquivo = open("automoveis.txt", "w")

for i in range(random.randint(5,15)):
    tipo = random.randint(1,4)
    km = random.randint(0,500)
    valor = str(tipo)+";"+str(km)
    arquivo.write("%s\n" % valor)

arquivo = open("automoveis.txt", "r")

c = 1
carrosLocados = 0
for linha in arquivo.readlines():
    tipo = 0
    km = ''
    for j in range(len(linha)):
        if j == 0:
            tipo = linha[j]
        else:
            if linha[j] != ";":
                km += linha[j]
    km = int(km)
    tipo = int(tipo)
    if km != 0:
        if tipo == 1:
            print('O carro da linha',c,'gasta:',km/8,'litros de gasolina.')
        elif tipo == 2:
            print('O carro da linha',c,'gasta:',km/10,'litros de gasolina.')
        elif tipo == 3:
            print('O carro da linha',c,'gasta:',km/15,'litros de gasolina.')
        else:
            print('O carro da linha',c,'gasta:',km/18,'litros de gasolina.')
        carrosLocados += 1
    c+=1

print('A quantidade de carros locados é de:',carrosLocados)

arquivo.close()