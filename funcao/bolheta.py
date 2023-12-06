def bolha(list):
    length = len(list)
    switch = True
    while switch and length > 0:
        switch = False
        for i in range(length-1):
            if list[i] > list[i+1]:
                switch = True
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
        length -= 1
    return list

vetor = [2,4,5,1,6,3,2,1,7,9,7,8]
print(bolha(vetor))