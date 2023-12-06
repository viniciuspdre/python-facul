import os, random
os.system('cls')


# firstSet = []
# secSet = []
# for add in range(10):
#     firstSet.append(random.randint(1,100))
#     secSet.append(random.randint(1,100))

# print(firstSet,'\n',secSet)

def multiplePair(firstArray, secondArray):
    if (firstArray % secondArray == 0 or secondArray % firstArray == 0):
        return True
    else:
        return False

count = 0
for j in range(10):
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)
    print('Are',n1,'and',n2,'multiples?')
    if multiplePair(n1,n2) == True:
        count += 1
    print(multiplePair(n1,n2))


print('\nO total de múltiplos é:',count)
        
# check = multiplePair(firstSet,secSet)
# print(check)