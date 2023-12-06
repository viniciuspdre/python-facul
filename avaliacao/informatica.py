import os, random
os.system('cls')

notasAlunos = []
freqAlunos = []
reprovados = 0
recuperacao = 0
aprovados = 0
somaMedia = 0

for i in range(40):
    notasAlunos.append(random.randint(0,10))
    freqAlunos.append(random.randint(100,200)) #coloquei de 100 a 200 horas, porque se não maior parte dos alunos nao seriam aprovados por carga horaria
    print('Aluno',i+1,'\nNota:',notasAlunos[i],'\nFrequência:',freqAlunos[i])

for j in range(len(notasAlunos)):
    somaMedia += notasAlunos[j]
    if notasAlunos[j] < 4 or freqAlunos[j] < 0.7*200:
        reprovados += 1
    elif notasAlunos[j] < 7 and freqAlunos[j] > 0.7*200:
        recuperacao += 1
    else:
        aprovados += 1

print('\n==================================================\n\nMédia:',somaMedia/len(notasAlunos))
print('Aprovados:',aprovados,'\nRecuperação:',recuperacao,'\nReprovados:',reprovados)