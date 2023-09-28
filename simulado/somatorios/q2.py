import os
os.system('cls')

def potencia(valor,expoente):
    produto = 1
    for i in range(expoente):
        produto*=valor
    return produto

exp = 1
den = 50
soma = 0
for i in range(50):
    potenciacao = potencia(2,exp)
    soma += potenciacao/den
    exp += 1
    den -= 1

print(soma)