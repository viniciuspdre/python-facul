import os
os.system('cls')

temp = float(input('Qual a temperatura da água?\n'))

if(temp < 0):
    print('A água está no estado sólido.')
elif(temp <= 100):
    print('A água está no estado líquido.')
else:
    print('A água está no estado gasoso.')