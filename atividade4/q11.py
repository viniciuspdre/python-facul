import random
lucro = 0; carro = 0; moto = 0; onibus = 0
for veiculo in range(1,401):
    opcao = random.randint(1,3)
    if opcao == 1:
        lucro = lucro + 4
        moto = moto + 1
    elif opcao == 2:
        lucro = lucro + 8
        carro = carro + 1
    elif opcao == 3:
        lucro = lucro + 20
        onibus = onibus + 1
    # else:
    #     print('Erro na escolha da opção') Eu escolhi retirar o else porque como o valor foi randomico ele não vai sair do range informado
print('O número de motos estacionadas foi:',moto,'\nO número de carros estacionados foi:',carro,'\nO número de ônibus estacionado foi:',onibus,'\nO lucro do estacionamento foi R$',lucro)