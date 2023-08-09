import os
os.system('cls')

carro = input('Digite o nome do carro que o Batman escolheu (Morcego Preto | Vampiro Voador): ')

if(carro.lower() == 'morcego preto'):
    print('O Batman gastará: ', 300+(295/16)*0.75)
elif(carro.lower() == 'vampiro voador'):
    print('O Batman gastará: ', 500+(295/11)*0.75)
else:
    print('Digite um carro válido!')