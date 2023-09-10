import os
os.system('cls')

palavra = input('Forneça uma palavra: ')
consonant = 0

for i in palavra:
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        consonant += 1

print(consonant)