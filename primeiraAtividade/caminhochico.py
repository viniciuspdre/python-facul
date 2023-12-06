import os
os.system('cls')

print('Esse software verificará quanto tempo Chico Bento demorará para chegar à escola.')
botina = int(input('O Chico vai andar de botina? Se sim, digite 1, se não digite 0.\n'))
os.system('cls')
teobaldo = int(input('O Chico vai andar no Teobaldo? Se sim, digite 1, se não digite 0.\n'))
os.system('cls')
riacho = int(input('O Chico vai parar no riacho? Se sim, digite 1, se não digite 0.\n'))
os.system('cls')
pomar = int(input('O Chico vai entrar no pomar do Nhô Lau? Se sim, digite 1, se não digite 0.\n'))
os.system('cls')
rosinha = int(input('O Chico vai se encontrar com a Rosinha? Se sim, digite 1, se não digite 0.\n'))
os.system('cls')
onca = int(input('Por fim, ele vai ser surpreendido pela onça? Se sim, digite 1, se não digite 0.\n'))
os.system('cls')

if(botina == 0 and teobaldo == 0):
    tempo = 50
    if(riacho == 1 and pomar == 1 and rosinha == 1 and onca == 1):
        tempo += 40
    elif(riacho == 1 and pomar == 1 and rosinha == 1):
        tempo += 70
    elif(riacho == 1 and pomar == 1):
        tempo += 60
    elif(riacho == 1):
        tempo += 40
    print('O tempo que o Chico vai demorar para chegar à escola será {0} minutos'.format(tempo))
elif(botina == 1 and teobaldo == 0):
    tempo = 40
    if(riacho == 1 and pomar == 1 and rosinha == 1 and onca == 1):
        tempo += 40
    elif(riacho == 1 and pomar == 1 and rosinha == 1):
        tempo += 70
    elif(riacho == 1 and pomar == 1):
        tempo += 60
    elif(riacho == 1):
        tempo += 40
    print('O tempo que o Chico vai demorar para chegar à escola será {0} minutos'.format(tempo))
elif(botina == 0 and teobaldo == 1):
    tempo = 30
    if(riacho == 1 and pomar == 1 and rosinha == 1 and onca == 1):
        tempo += 40
    elif(riacho == 1 and pomar == 1 and rosinha == 1):
        tempo += 70
    elif(riacho == 1 and pomar == 1):
        tempo += 60
    elif(riacho == 1):
        tempo += 40
    print('O tempo que o Chico vai demorar para chegar à escola será {0} minutos'.format(tempo))
else:
    tempo = 30
    if(riacho == 1 and pomar == 1 and rosinha == 1 and onca == 1):
        tempo += 40
    elif(riacho == 1 and pomar == 1 and rosinha == 1):
        tempo += 70
    elif(riacho == 1 and pomar == 1):
        tempo += 60
    elif(riacho == 1):
        tempo += 40
    print('O tempo que o Chico vai demorar para chegar à escola será {0} minutos'.format(tempo))