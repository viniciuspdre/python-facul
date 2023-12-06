#caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

import os
os.system('cls')


palavra = input('Olá usuário, nesse programa você pode fornecer uma palavra ou uma frase para que ela seja manipulada: ')

def minuscula(string):
    contador = 0
    alfabetoMaiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alfabetoMinusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    novaString = ''
    for i in range(len(string)):
        for j in range(len(alfabetoMaiusculo)):
            if string[i] == alfabetoMaiusculo[j]:
                novaString += alfabetoMinusculo[j]
                contador += 1
        if contador == 0:
            novaString += string[i]
        else:
            contador = 0
    string = novaString
    return string

def vertical(string):
    for i in range(len(string)):
        print(string[i])

def diagnonal(string,contador=0):
    for i in range(len(string)):
        print(' '*contador+string[i])
        contador += 1

def diagonalInvertida(string,contador=0):
    tamanho = len(string)
    for i in range(len(string)):
        print(' '*tamanho+contador*' '+string[i])
        tamanho -= 1    

def contraria(string):
    tamanho = len(string)
    for i in range(len(string)):
        print(string[tamanho-1],end='')
        tamanho -= 1

def semEspaco(string):
    for i in range(len(string)):
        if string[i] != ' ':
            print(string[i],end='')

def semVogal(string):
    for i in range(len(string)):
        if string[i] != 'a' and string[i] != 'A' and string[i] != 'e' and string[i] != 'E'and string[i] != 'i' and string[i] != 'I' and string[i] != 'o' and string[i] != 'O' and string[i] != 'u' and string[i] != 'U':
            print(string[i],end='')

def vogalAst(string):
    for i in range(len(string)):
        if string[i] != 'a' and string[i] != 'A' and string[i] != 'e' and string[i] != 'E'and string[i] != 'i' and string[i] != 'I' and string[i] != 'o' and string[i] != 'O' and string[i] != 'u' and string[i] != 'U':
            print(string[i],end='')
        else:
            print('*',end='')

def contarPalavras(string):
    contador = 1
    for i in range(len(string)):
        if string[i] == ' ':
            contador += 1
    return contador

def palavrasFrase(string):
    palavras = []
    palavra = ''
    tamanho = len(string)
    for i in range(len(string)):
        if i == tamanho-1:
            palavra += string[i]
            palavras.append(palavra)
        elif string[i] != ' ':
            palavra += string[i]
        else:
            palavras.append(palavra)
            palavra = ''
    return palavras

def maiorPalavra(string):
    indiceMaior= -1
    contadores = []
    contador = 0
    palavras = []
    palavra = ''
    tamanho = len(string)
    for i in range(len(string)):
        if i == tamanho-1:
            palavra += string[i]
            palavras.append(palavra)
            contadores.append(contador)
        elif string[i] != ' ':
            palavra += string[i]
            contador += 1
        else:
            palavras.append(palavra)
            palavra = ''
            contadores.append(contador)
            contador = 0
    for j in range(len(contadores)-1):
        if contadores[j] > contadores[j+1]:
            indiceMaior = j
        else:
            indiceMaior = j+1
    return palavras[indiceMaior]

def trocarPalavra(string, oldString, newString):
    fraseNova = palavrasFrase(string) #aqui estou pegando o array com as palavras
    for i in range(len(fraseNova)):
        if fraseNova[i] == oldString:
            fraseNova[i] = newString
    for j in range(len(fraseNova)):
        print(fraseNova[j]+' ', end='')

def iniciaMaiusculo(string):
    agora = minuscula(string)
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']
    alfabetoMaiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alfabetoMinusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    novaString = ''
    contador = 0
    for i in range(len(agora)):
        for j in range(len(alfabetoMaiusculo)):
            if i == 0 and agora[i] == alfabetoMinusculo[j]:
                novaString += alfabetoMaiusculo[j]
                contador = 1
        for k in range(len(numeros)):
            if agora[i] == numeros[k]:
                novaString += numeros[k]
        if agora[i] == ' ':
                novaString += ' '
                contador = 2
        if contador == 0:
            novaString += agora[i]
        elif contador == 2:
            for j in range(len(alfabetoMaiusculo)):
                if agora[i] == alfabetoMinusculo[j]:
                    novaString += alfabetoMaiusculo[j]
                    contador = 0
                    break
        else:
            contador = 0
    return novaString

def fraseVertical(string):
    updating = palavrasFrase(string)
    cadaPalavra = ''
    contador = 0
    for i in range(len(updating)):
        cadaPalavra = updating[i]
        for j in range(len(cadaPalavra)):
            print(contador*' '+cadaPalavra[j])
        contador += 1

def contarCar(string, char):
    contador = 0
    for i in range(len(string)):
        if string[i] == char:
            contador += 1
    return contador

def palavrasZigZag(string):
    updating = palavrasFrase(string)
    for i in range(len(updating)):
        if i % 2 == 0:
            print(updating[i],end='')
        else:
            inversa = updating[i]
            tam = len(inversa)
            c = 0
            for j in range(len(inversa)):
                print(inversa[tam-1-c], end='')
                c += 1
        print(' ',end='')

def vogaisMaiusculas(string):
    contador = 0
    vogaisMaius = ['A', 'E','I','O','U']
    vogaisMinus = ['a','e','i','o','u']
    string = minuscula(string)
    novaString = ''
    for i in range(len(string)):
        for j in range(len(vogaisMinus)):
            if string[i] == vogaisMinus[j]:
                novaString += vogaisMaius[j]
                contador = 1
        if contador == 0:
            novaString += string[i]
        else:
            contador = 0
    return novaString

def posicaoVogal(string):
    pos = -1
    string = minuscula(string)
    for i in range(len(string)):
        if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
            pos = i
    if pos == -1:
        return 'Não há vogal na frase ou palavra.'
    else:
        return pos
    
def somaNaoVogais(string):
    res = 0
    string = minuscula(string)
    for i in range(len(string)):
        if string[i] != 'a' and string[i] != 'e' and string[i] != 'i' and string[i] != 'o' and string[i] != 'u' and string[i] != ' ':
            res += i
    return res

def palavraCentral(string):
    palavras = palavrasFrase(string)
    tam = len(palavras)
    if tam % 2 != 0:
        print('=========================')
        return 'Palavra central: '+palavras[int((tam-1)/2)]
    
def priUltDiag(string):
    string = palavrasFrase(string)
    palavraInicio = string[0]
    palavraFinal = string[len(string)-1]
    if len(string) == 0:
        return 'Não foi fornecido palavra'
    elif len(string) == 1:
        return diagnonal(palavraInicio)
    else:
        return diagnonal(palavraInicio), diagnonal(palavraFinal,len(palavraInicio))
    
def silabas(string):
    string = palavrasFrase(string)
    palavrinha = ''
    contador = 0
    for i in range(len(string)):
        palavrinha = string[i]
        if len(palavrinha) % 2 == 0:
            for j in range(len(palavrinha)):
                if contador == 2:
                    print(' '+palavrinha[j],end='')
                    contador = 0
                else:
                    print(palavrinha[j],end='')
                    contador += 1

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

def descript(string):
    string = cifraDeCesar(string)
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

def priUltVert(string):
    string = palavrasFrase(string)
    palavraInicio = string[0]
    palavraFinal = string[len(string)-1]
    if len(string) == 0:
        return 'Não foi fornecido palavra'
    elif len(string) == 1:
        return vertical(palavraInicio)
    else:
        return vertical(palavraInicio), vertical(palavraFinal)

def priUltDiagInv(string):
    string = palavrasFrase(string)
    palavraInicio = string[0]
    palavraFinal = string[len(string)-1]
    if len(string) == 0:
        return 'Não foi fornecido palavra'
    elif len(string) == 1:
        return diagonalInvertida(palavraInicio)
    else:
        return diagonalInvertida(palavraInicio,len(palavraFinal)), diagonalInvertida(palavraFinal)
    
def tornado(string):
    c = 0
    contador = 0
    for i in range(len(string)):
        if c == 0:
            print(' '*contador+string[i])
            c = 1
        else:
            print((len(string)-contador-1)*' '+string[i])
            c = 0
            contador += 1

vertical(palavra)
print('=========================')
diagnonal(palavra)
print('=========================')
diagonalInvertida(palavra)
print('=========================')
contraria(palavra)
print('\n=========================')
semEspaco(palavra)
print('\n=========================')
semVogal(palavra)
print('\n=========================')
vogalAst(palavra)
print('\n=========================')
print('Quantidade de palavras na frase:',contarPalavras(palavra))
print('=========================')
print('A maior palavra é:',maiorPalavra(palavra))
print('=========================')
trocarPalavra(palavra, 'nome', 'idade')
print('\n=========================')
print('A frase em minúsculo:',minuscula(palavra))
print('=========================')
print('A frase com cada palavra com a primeira letra maiúscula:',iniciaMaiusculo(palavra))
print('=========================')
fraseVertical(palavra)
print('=========================')
print(contarCar(palavra, 'c'))
print('=========================')
palavrasZigZag(palavra)
print('\n=========================')
print(vogaisMaiusculas(palavra))
print('=========================')
print('Posição que está a última vogal:',posicaoVogal(palavra))
print('=========================')
print('A soma dos índices das não vogais é:',somaNaoVogais(palavra))
print(palavraCentral(palavra))
print('=========================')
priUltDiag(palavra)
print('=========================')
print('Palavras com as sílabas separdas:')
silabas(palavra)
print('\n=========================')
print('Palavra criptografada:', cifraDeCesar(palavra))
print('=========================')
print('Palavra descriptografada:', descript(palavra))
print('=========================')
priUltVert(palavra)
print('=========================')
priUltDiagInv(palavra)
print('=========================')
tornado(palavra)