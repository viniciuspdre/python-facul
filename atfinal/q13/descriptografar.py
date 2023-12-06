import os
os.system('cls')

def descript(string):
    caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    novaString = ''
    for i in range(len(string)):
        for j in range(len(caracteres)):
            if string[i] == caracteres[j]:
                if j == 0:
                    novaString += caracteres[len(caracteres)-3]
                elif j == 1:
                    novaString += caracteres[len(caracteres)-2]
                elif j == 2:
                    novaString += caracteres[len(caracteres)-1]
                else:
                    novaString += caracteres[j-3]
        if string[i] == ' ':
            novaString += ' '
    string = novaString
    return string

arquivo = open('atfinal/q13/arquivoNovo.txt','r')
novoArquivo = open('atfinal/q13/arquivoDescript.txt','w')

frase = ''
for linha in arquivo.readlines():
    frase = linha
    novoArquivo.write('%s\n'%descript(frase))

novoArquivo.close()
arquivo.close()