def potencia(base,expoente):
    res = 1
    if expoente > 0:
        for i in range(expoente):
            res *= base
    elif expoente < 0:
        expoente *= -1
        for i in range(expoente):
            res *= base
    return res

soma = 0
for i in range(3):
    b = int(input('Digite o valor da base: '))
    e = int(input('Digite o valor do expoente: '))
    soma += potencia(b,e)

print(soma)