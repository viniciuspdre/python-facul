import os
os.system('cls')

arquivoHomem = open('homem.txt','a')
arquivoMulher = open('mulher.txt','a')
for i in range(10):
    sexo = int(input('Digite 1 para masculino e 2 para feminino: '))
    nome = input('Digite o nome: ')
    if sexo == 1:
        arquivoHomem.write('%s\n' % nome)
    else:
        arquivoMulher.write('%s\n' % nome)
arquivoHomem.close()
arquivoMulher.close()    