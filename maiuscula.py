import os
os.system('cls')

def separar(string):
    palavra = ''
    palavras = []
    for i in range(len(string)):
        if string[i] == ' ':
            palavras.append(palavra)
            palavra = ''
        elif i == len(string)-1:
            palavra += string[i]
            palavras.append(palavra)
        else:
            palavra += string[i]
    return palavras

def palavraMaius(string):
    palavrasSep = separar(string)
    novaString = ''
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(palavrasSep)):
        palavra = palavrasSep[i]
        for j in range(len(palavra)):
            for k in range(len(minusculas)):
                if palavra[j] == minusculas[k]:
                    novaString += maiusculas[k]
                elif palavra[j] == maiusculas[k]:
                    novaString += palavra[j]
        novaString += ' '
    return novaString

print(palavraMaius('o senhor E Meu pastor e nada me faltara'))