numbers = [1,2,3,4,5,6,7,8,9]

length = len(numbers)
c=0
for i in range(len(numbers)):
    for j in range(length-1-c):
        aux = numbers[j]
        numbers[j] = numbers[j+1]
        numbers[j+1] = aux
    c+=1

print(numbers)