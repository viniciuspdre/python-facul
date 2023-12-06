import os
os.system('cls')

def cifraDeCesar(string):
    novaString = ''
    caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(string)):
        for j in range(len(caracteres)):
            if string[i] == caracteres[j]:
                if j == len(caracteres)-1:
                    novaString += caracteres[2]
                elif j == len(caracteres)-2:
                    novaString += caracteres[1]
                elif j == len(caracteres)-3:
                    novaString += caracteres[0]
                else:
                    novaString += caracteres[j+3]
        if string[i] == ' ':
            novaString += ' '
    string = novaString
    return string

arquivo = open('atfinal/q13/arquivoNovo.txt','w')
frase = 'eu gosto de feijao'
arquivo.write('%s'%cifraDeCesar(frase))

arquivo.close()