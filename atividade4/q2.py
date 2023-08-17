import random, os

os.system('cls')

mago = random.randint(1000,4000); dragao = random.randint(1000,4000); genio = random.randint(1000,4000); caveiraNegra = random.randint(1000,4000)
yugi = 0; kaiba = 0; i = 0

while i < 2 or kaiba == yugi:
    if(i % 2 == 0):
        while mago == genio:
            mago = random.randint(1000,4000)
            genio = random.randint(1000,4000)
        if(mago > genio):
            yugi += 1
        else:
            kaiba += 1
    if(i % 2 == 1):
        while dragao == caveiraNegra:
            dragao = random.randint(1000,4000)
            caveiraNegra = random.randint(1000,4000)
        if(caveiraNegra > dragao):
            yugi += 1
        else:
            kaiba += 1
    i += 1


print(kaiba,yugi)
if(yugi > kaiba):
    print('Yami foi o vencedor do duelo.')
else:
    print('Kaiba foi o vencedor do duelo.')