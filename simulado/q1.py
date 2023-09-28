import random, os
os.system('cls')

print('Bem vindo, usuário, esse programa foi feito para que você crie um conjunto com valores aleatórios do tamanho que você desejar e depois tire valores indesejados.')
valores = []
n = int(input('Quantos números você deseja adicionar no conjunto?\n'))
print('Conjunto: ',end='')
for add in range(n):
    valores.append(random.randint(1,100))
    print(valores[add],'| ',end='')

confirm = 1
contador = 0
while confirm == 1:
    pos = int(input(('\nDigite a posição do número que você deseja retirar.\nExemplo: Se deseja retirar o primeiro número é só digitar 1!\nFique à vontade para digitar a posição...\n')))
    pos = pos - 1 - contador
    novoValores = []
    for i in range(len(valores)):
        if i != pos:
            novoValores.append(valores[i])
    valores = novoValores
    confirm = int(input('Caso você deseja excluir mais um número digite 1, entretanto, se deseja ver o conjunto com o/os número(s) que você retirou digite 0.'))
    contador += 1

print(valores)