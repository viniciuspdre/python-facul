# + + + - - + + - -
c = 0
soma = 0

for i in range(1,51):
    if c <= 2:
        print(' +',i,end='')
        soma += i
    elif c <= 4:
        print(' -',i,end='')
        soma -= i
    elif c <= 6:
        print(' +',i,end='')
        soma += i
    elif c <= 7:
        print(' -',i,end='')
        soma -= i
    else:
        print(' -',i, end='')
        soma -= i
        c = -1
    c+=1
print('=',soma,end='')