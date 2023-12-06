import os 
os.system('cls')
x = 1
y = x*2
sinal = 0
op = '+'

print('{0}/{1} '.format(x,y,op),end='')

for i in range(1, 30):
    x+=1
    y=x*2
    if(sinal == 0):
        print('-{0}/{1} '.format(x,y,op),end='')
        sinal = 1
    else:
        print('+{0}/{1} '.format(x,y,op),end='')
        sinal = 0