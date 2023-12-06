import os, random
os.system('cls')

#acredito que os cada semente fere uma arvore que produza de 30 a 100 frutos

sementes = 490
passaros = random.randint(1,89)
pedregoso = random.randint(100,200)
pedregosoFrutos = random.randint(6,20) #1/5 dos frutos normais
espinhos = random.randint(80,148) #removendo os 20%

sementes = sementes-(passaros+pedregoso+espinhos)

totalDeFrutos = (pedregoso*pedregosoFrutos)+sementes*random.randint(30,100)

print('O total de filhos que o agricultor levou para o pai foi de:',totalDeFrutos*500)