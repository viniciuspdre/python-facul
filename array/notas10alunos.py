import os, random
os.system('cls')

notasAlunos = []
notasCalc = []
soma = 0
passou = 0

for i in range(10):
    for j in range(4):
        notaAluno = random.randrange(0,10)
        notasCalc.append(notaAluno)
        soma += notasCalc[j]
        media = soma/len(notasCalc)
    notasAlunos.append(media)
    if notasAlunos[i] >= 7:
        passou += 1
    soma = media = 0
    notasCalc.clear()

print('Notas:',notasAlunos,'\nPassaram:',passou)