import os
os.system('cls')

notas = []
i = 1

while i < 5:
    nota = float(input('Me forneça sua nota: '))
    notas.append(nota)
    i+=1

soma = 0
for j in range(len(notas)):
    soma += notas[j]

print('Média:',(soma/len(notas)))