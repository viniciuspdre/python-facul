import os, random
os.system('cls')

vovo = 0
lucro = 0

for i in range(3):
    moto = 0
    carro = 0
    caminhao = 0
    for j in range(100):
        valor = random.randint(1,3)
        if valor == 1:
            rodas = random.randint(1,2)
            moto += rodas
        elif valor == 2:
            rodas = random.randint(1,4)
            carro += rodas
        else:
            rodas = random.randint(1,8)
            caminhao += rodas
    
    lucroNovo = moto*10+carro*15+caminhao*50
    if lucroNovo > 1000:
        vovo += 0.34*lucroNovo
        lucroNovo *= 0.66
    if lucroNovo > lucro:
        lucro = lucroNovo
    
print('Maior lucro obtido:',lucro)
print('Total recebido pela vovó Bondade:',vovo)