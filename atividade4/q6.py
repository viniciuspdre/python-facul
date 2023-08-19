import os

os.system('cls')

idade = 0
nome = ''
confirm = ''

while confirm != 'sim':
    thisNome = input('Forneça o nome da pessoa: ')
    thisIdade = int(input('Forneça a idade da pessoa: '))
    if(thisIdade % 2 == 0):
        if(thisIdade > idade):
            nome = thisNome
            idade = thisIdade
    else:
        print('Essa pessoa não tem idade par.')
    confirm = input('Você deseja sair do programa? (Se sim, digite sim todo em minúsculo, se não, digite qualquer coisa.)')

print('O nome da pessoa mais velha com idade par é: ', nome)