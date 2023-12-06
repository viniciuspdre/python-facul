import os, random
os.system('cls')

def jogada():
    bola = random.randint(1,30)
    raquete = [random.randint(1,21)]
    for i in range(9):
        raquete.append(raquete[i]+1)
    contador = 0
    for j in range(len(raquete)):
        if raquete[j] == bola:
            return True
        else:
            contador += 1
        if contador == len(raquete):
            return False

jogador1 = 'Pedro'
jogador2 = 'Maria'
pontosJogador1 = 0; pontosJogador2 = 0
vez = 1

while pontosJogador1 < 11 and pontosJogador2 < 11:
    if vez == 1:
        jogar = jogada()
        if jogar:
            vez = 2
        else:
            pontosJogador1 += 1
            vez = 2
    else:
        jogar = jogada()
        if jogar:
            vez = 1
        else:
            pontosJogador2 += 1
            vez = 1

if pontosJogador1 == 11:
    print('Parabéns o(a) vencedor(a) foi:',jogador1)
    print('Placar:',jogador1,pontosJogador1,'|',jogador2,pontosJogador2)
else:
    print('Parabéns o(a) vencedor(a) foi:',jogador2)
    print('Placar:',jogador1,pontosJogador1,'|',jogador2,pontosJogador2)