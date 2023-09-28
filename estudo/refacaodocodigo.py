# #- Sabendo que a fórmula para calcular o peso ideal é:
# ➢ Para mulheres: (62.1 * altura) – 44.7;
# ➢ Para homens: (72.2 * altura) – 58;
# Faça um programa que recebe o sexo e a altura de uma pessoa e informe o peso ideal

def calculo():
    sexo=int(input('Digite 1 para homem e 0 para mulher.'))
    if sexo==1:
        altura=float(input('Digite a altura da pessoa: '))
        print('O peso ideal do cara é: ',(72.2 * altura)-58)
    elif sexo==0:
        altura=float(input('Digite a altura da pessoa: '))
        print('O peso ideal da monah é: ',(62.1 * altura)-44.7)
    else:
        print('Tá errado pae')

conf=1

while conf==1:
    calculo()
    conf=int(input('Quer continuar? 1=Sim / 0=Não'))