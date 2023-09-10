import os
os.system('cls')

anos = []
aux = 0

for i in range(1997, 2501):
    anos.append(i)

for x in range(len(anos)):
    if anos[x]%4==0:
        aux+=1

conta = 126*366+(504-126)*365
print(aux)
print((conta - 366)%7)