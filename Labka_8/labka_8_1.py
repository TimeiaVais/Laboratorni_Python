# Визначити кількість додатних елементів матриці з першим парним і другим
a=[ #0 1 2
    [1,4,2],   #0
    [3,1,7],   #1
    [5,6,1]    #2
]
k = 0
for i in range(len(a)):
    for j in range(0,len(a[i])):
        if (a[i][j] %2 == 0) :
            k +=1
        else:
            0
print('Кількість додатних елементів: {0}'.format(k))