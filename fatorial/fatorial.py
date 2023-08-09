import os
os.system('cls')

fat = 1
x = int(input('Froneça um número para que seja calculado o fatorial do mesmo: '))
i = 1

# while i <= x:
#     fat = fat * i
#     i+=1

for i in range(1, x+1):
    fat*=i

print(fat) 