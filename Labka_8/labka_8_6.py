'''
s -  кількість рядків матриці
l - кількість стовпців матриці
a - матриця
suma - сума
sum_neg - функція знаходженння суми
'''
s = int(input('Введіть кількість рядків матриці:  '))
l = int(input('Введіть кількість стовпців матриці:  '))
a = [[int(input('Введіть елемент матриці у {0} рядку та у {1} стовпці:  '.format(nn,n))) for n in range(l)] for nn in range(s)] #ввід елементів
counter = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if i <= j:
            if  0 < i < len(a) or 0 < j < len(a[i]):
                for k in range(j-1,j+1):
                    if a[i][j] < a[i][j]:
                        counter += abs(a[i][j])
                for k in range(i-1,i+1):
                    for el in range(len(a[k])):
                         if  a[i][j] < a[k][el]:
                             counter += abs(a[i][j])
print('Сума - ',counter)