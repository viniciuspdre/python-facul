vetor = [0,1,2,3,4,5,6,7,8,9]

tam = len(vetor)

for j in range(tam):
    for i in range(tam-1):
        aux = vetor[i]
        vetor[i] = vetor[i+1]
        vetor[i+1] = aux
    tam -= 1

print(vetor)