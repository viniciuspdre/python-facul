import os
os.system('cls')

fat = 1
x = int(input('Froneça um número para que seja calculado o fatorial do mesmo: '))

# while i <= x:
#     fat = fat * i
#     i+=1

print('Fatorial de ', end='')
for i in range(x):
    print(x-i,end=' x ')
    fat*=i+1

print('=', fat) 