def calculoIMC(sexo,altura):
    if sexo == 0:
        return (62.1*altura)-44.7
    elif sexo == 1:
        return (72.2*altura)-58
    else:
        return 'Você informou um valor inválido para o sexo.'

i = 1

while i == 1:
    s = int(input('Se você deseja calcular o peso ideal para uma mulher digite 0.\nCaso queira saber o peso idela de um homem digite 1.\n'))
    h = float(input('Digite a altura desta pessoa: '))
    pesoIdeal = calculoIMC(s,h)
    print(pesoIdeal)
    i = int(input('Se você deseja continuar no programa digite 1.\nSe você não deseja continuar digite 0.\n'))

