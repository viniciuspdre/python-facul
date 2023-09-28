import os
os.system('cls')

def somaPotencia(bases,expoentes):
    produto = 1
    produtos = []
    soma = 0
    for rodadas in range(len(bases)):
        if expoentes[rodadas] > 0:
            for i in range(expoentes[rodadas]):
                produto *= bases[rodadas]
        elif expoentes[rodadas] < 0:
            expoentes[rodadas] *= -1
            for i in range(expoentes[rodadas]):
                produto *= 1/bases[rodadas]
        else:
            produto = 1
        produtos.append(produto)
        produto = 1
        soma += produtos[rodadas]
    return soma

bss = []
exps = []
for i in range(3):
    bs = int(input('Digite o valor da base: '))
    print('Digite o valor do expoente de',bs,': ',end='')
    exp = int(input())
    bss.append(bs)
    exps.append(exp)

print('A soma é:',somaPotencia(bss,exps))
