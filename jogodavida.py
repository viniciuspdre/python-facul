import random, os
os.system('cls')

sort = random.randrange(1,8) #vai sortear uma profissão de 1 a 7, já que são sete profissões
match sort:
    case 1:
        print('Você foi sorteado para ser médico no jogo da vida.')
    case 2:
        print('Você foi sorteado para ser jornalista no jogo da vida.')
    case 3:
        print('Você foi sorteado para ser advogado no jogo da vida.')
    case 4:
        print('Você foi sorteado para ser professor no jogo da vida.')
    case 5:
        print('Você foi sorteado para ser físico no jogo da vida.')
    case 6:
        print('Você foi sorteado para ser comerciante no jogo da vida.')
    case 7:
        print('Você foi sorteado para ser estudante no jogo da vida.')
caminho = input('Se você deseja escolher o caminho A, digite a.\nSe você deseja escolher o caminho B, digite b.\n')

if caminho.lower() == 'a':
    match sort:
        case 1:
            pagamento = 50*20+25*10
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 2:
            pagamento = 24*20+12*10
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 3:
            pagamento = 50*20+25*10
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 4:
            pagamento = 24*20+12*10
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 5:
            pagamento = 30*20+15*10
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 6:
            pagamento = 12*20+6*10
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 7:
            pagamento = 16*20+8*10
            print('Seu pagamento foi: {0}'.format(pagamento))
elif caminho.lower() == 'b':
    match sort:
        case 1:
            pagamento = 50*20+25*5
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 2:
            pagamento = 24*20+12*5
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 3:
            pagamento = 50*20+25*5
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 4:
            pagamento = 24*20+12*5
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 5:
            pagamento = 30*20+15*5
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 6:
            pagamento = 12*20+6*5
            print('Seu pagamento foi: {0}'.format(pagamento))
        case 7:
            pagamento = 16*20+8*5
            print('Seu pagamento foi: {0}'.format(pagamento))
else:
    print('Digite um valor dentro do esperado (A ou B) para o caminho...')