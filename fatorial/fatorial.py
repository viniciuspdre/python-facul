import os
os.system('cls')

fat = 1
x = int(input('Froneça um número para que seja calculado o fatorial do mesmo: '))
i = 1

# while i <= x:
#     fat = fat * i
#     i+=1

print('Fatorial de: ',x, end='')

for i in range(1, x+1):
    fat*=i
    if(x-i==0):
        continue
    print(' x', x - i,end=' ')

print('=', fat) 