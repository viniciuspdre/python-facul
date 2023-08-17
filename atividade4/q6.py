import os

os.system('cls')

idade = 0
nome = ''
confirm = ''

while confirm != 'sim':
    thisNome = input('Forneça o nome da pessoa: ')
    thisIdade = int(input('Forneça a idade da pessoa: '))
    if(thisIdade > idade):
        idade = thisIdade
        nome = thisNome
    confirm = input('Você deseja sair do programa? (Se sim, digite sim todo em minúsculo, se não, digite qualquer coisa.)')

print('O nome da pessoa mais velha é: ', nome)