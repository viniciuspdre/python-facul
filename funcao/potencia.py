import os
os.system('cls')

def potencia(base, expoente):
    res = 1
    if expoente >= 0:
        for i in range(expoente):
            if expoente>0:
                res *= base
            else:
                res = 1
        return res
    else:
        expoente *= -1
        for i in range(expoente):
            res *= 1/base
        return res
        
print(potencia(2,10))
            