import os, random
os.system('cls')

def remove(array,index):
    newArray = []
    for i in range(len(array)):
        if index != i:
            newArray.append(array[i])
    array = newArray
    return array

alunos = ['adryan','arthur','camille','caio','cayky','tereza','jakelyne','ruan','italo','wellison','pedro','gustavo','rodinei','luandra','suzana','ritinha','marielle','joao','jota','cleber','maristela','claybson','felipe','tonho','tonha','homer simpson']
lab_1 = []; lab_2 = []


tamanhoMetade = int(len(alunos)/2)
for i in range(len(alunos)):
    escolhaLab = random.randint(1,2)
    aluno = random.randint(0,len(alunos)-1)
    if len(lab_1) == tamanhoMetade:
        lab_2.append(alunos[aluno])
    elif len(lab_2) == tamanhoMetade:
        lab_1.append(alunos[aluno])
    else:
        if escolhaLab == 1:
            lab_1.append(alunos[aluno])
        else:
            lab_2.append(alunos[aluno])
    alunos = remove(alunos,aluno)
print(lab_1,'\n\n',lab_2)    