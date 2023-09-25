import os
os.system('cls')

def melhorCombustivel(kmlg, kmle, kmld, dist):
    print('O valor em real que você gastará usando gasolina é:',dist/kmlg*5.63)
    print('O valor em real que você gastará usando etanol é:',dist/kmle*3.87)
    print('O valor em real que você gastará usando diesel é:',dist/kmld*4.95)

i = 0
while i != 1:
    x = float(input('Forneça o consumo médio do carro em km/l usando gasolina: '))
    y = float(input('Forneça o consumo médio do carro em km/l usando etanol: '))
    z = float(input('Forneça o consumo médio do carro em km/l usando diesel: '))
    km = float(input('Digite a distância que você percorrerá: '))
    melhorCombustivel(x,y,z,km)

    i = int(input('Digite 1 para sair e 0 para continuar...\n')) 