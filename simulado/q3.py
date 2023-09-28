import os, random
os.system('cls')

alunos = []
confirm = 1

while confirm == 1:
    aluno = input('Digite o nome de um aluno: ')
    alunos.append(aluno)
    confirm = int(input('Você deseja continuar?\n1 - SIM | 2 - NÃO.\n'))

lab1Contador = 0; lab2Contador = 0
lab1 = [];lab2 = []
for i in range(len(alunos)):
    n = random.randint(1,2)
    if lab1Contador == int(len(alunos)/2):
        print('===============================================')
        print(alunos[i],'está no laboratório 2.')
        lab2Contador += 1
        lab2.append(alunos[i])
    elif lab2Contador == int(len(alunos)/2):
        print('===============================================')
        print(alunos[i],'está no laboratório 1.')
        lab1Contador += 1
        lab1.append(alunos[i])
    else:
        if n == 1:
            print('===============================================')
            print(alunos[i],'está no laboratório 1.')
            lab1Contador += 1
            lab1.append(alunos[i])
        else:
            print('===============================================')
            print(alunos[i],'está no laboratório 2.')
            lab2Contador += 1
            lab2.append(alunos[i])