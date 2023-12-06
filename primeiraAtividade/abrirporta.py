import random, os
os.system('cls')

esq = random.randrange(20, 51)
corc = random.randrange(20, 51)
braco = random.randrange(20, 51)
mroxa = random.randrange(20, 51)
senhora = random.randrange(20, 51)
musculoso = random.randrange(20, 51)

if(senhora + musculoso + 120 < esq + corc+ braco + mroxa):
    print('O quarteto conseguiu abrir a porta!')
else:
    print('O quarteto não conseguiu abrir a porta...')
