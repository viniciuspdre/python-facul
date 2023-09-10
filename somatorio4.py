#- - + - + + +

num = 1
den = 2
c = 0
res = 0

for i in range(1,51):
    if c <= 1:
        print(' - (', num, '/', den, end=')')
        res += -num/den
    elif c == 2:
        print(' + (', num, '/', den, end=')')
        res += num/den
    elif c == 3:
        print(' - (', num,'/',den,end=')')
        res += -num/den
    elif c <= 5:
        print(' + (', num,'/',den,end=')')
        res += num/den
    else:
        print(' + (', num,'/',den,end=')')
        res += num/den
        c = -1
    num += 1
    den += 2
    c += 1
print(' =', res,end='')