nomes = []
idades = []
ordem = ''

for i in range(10):
    match i:
        case 0:
            ordem = 'primeira'
        case 1:
            ordem = 'segunda'
        case 2:
            ordem = 'terceira'
        case 3:
            ordem = 'quarta'
        case 4:
            ordem = 'quinta'
        case 5:
            ordem = 'sexta'
        case 6:
            ordem = 'sétima'
        case 7:
            ordem = 'oitava'
        case 8:
            ordem = 'nona'
        case 9:
            ordem = 'décima'
    print('Forneça o nome da',ordem,'pessoa: ',end='')
    nome = input()
    nomes.append(nome)
    print('Forneça a idade de',nome,'para ordenarmos: ',end='')
    idade = int(input())
    idades.append(idade)

troca = 1
auxNome = ''
auxNum = 0
tamanho = len(nomes)

while troca == 1:
    troca = 0
    for j in range(tamanho-1):
        if nomes[j] > nomes[j+1]:
            auxNome = nomes[j+1]
            nomes[j+1] = nomes[j]
            nomes[j] = auxNome
            auxNum = idades[j+1]
            idades[j+1] = idades[j]
            idades[j] = auxNum
            troca = 1
    tamanho -= 1

for j in range(len(idades)):
    print('Nomes ordenados em ordem alfbética:',nomes[j],'| Idade:',idades[j],'\n')

print('===========================================================================\n')

tamanho = len(nomes)
troca = 1

while troca == 1:
    troca = 0
    for y in range(tamanho-1):
        if idades[y] > idades[y+1]:
            auxNome = nomes[y+1]
            nomes[y+1] = nomes[y]
            nomes[y] = auxNome
            auxNum = idades[y+1]
            idades[y+1] = idades[y]
            idades[y] = auxNum
            troca = 1
    tamanho -= 1

for x in range(len(idades)):
    print('Nomes ordenados por idade na ordem crescente:',nomes[x],'| Idade:',idades[x],'\n')