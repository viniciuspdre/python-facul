#1/2 + 2/4 + 3/6 - 4/8 + 5/10 - 6/12
n = 1
num1 = 1
num2 = 2

for i in range (1,50):
    if n <= 3:
        print('+',num1,'/',num2,'')
        num1+=1
        num2+=2
        n+=1
    elif n <=4:
        print('-',num1,'/',num2,'')
        num1+=1
        num2+=2
        n+=1
    elif n <=5:
        print('+',num1, '/',num2,'')
        num1+=1
        num2+=2
        n+=1
    else:
        print('-',num1, '/',num2,'')
        num1+=1
        num2+=2
        n=0
        n+=1
print (num1, '/', num2,)