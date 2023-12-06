vetor = [0,1,2,3,4,5,6,7,8,9,]
novoVetor = []
remover = int(input('Digite o índice do array que você deseja remover: '))

for i in range(len(vetor)):
    if i != remover:
        novoVetor.append(vetor[i])

vetor = novoVetor
print(vetor)