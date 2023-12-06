import os
os.system('cls')

arquivo = open('atfinal/aluno.txt', 'r')
letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

for linha in arquivo.readlines():
    nome = ''
    nota1 = ''
    nota2 = ''
    contagem = 0
    for i in range(len(linha)):
        if linha[i] != '|':
            nome += linha[i]
        if i < len(linha):
            for j in range(len(letras)):
                if linha[i] == letras[j] and contagem < 3:
                    nota1 += linha[i]
                    contagem += 1
                elif linha[i] != letras[j] and contagem == 3:
                    nota2 += linha[i]
    print('Nome:',nome,'| Nota 1:',nota1,'| Nota 2:',nota2)

arquivo.close()