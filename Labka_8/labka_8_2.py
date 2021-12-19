#Побудувати прямокутну матрицю А, елементи якої задаються формулою:
# a_i_j = i!-j! i,j = 1,N
#Обчислити суму елементів матриці А, сума індексів яких непарна.
n = int(input('n = '))
a = []
from math import factorial
for i in range(n):
    row = []
    for j in range(n):
        row.append(factorial(i) - factorial(j))
    a.append(row)
a=[[ factorial(i) - factorial(j) for j in range(n)] for i in range(n)]
print(*a, sep='\n')
s = 0
for i in range(1,len(a),2):
    for j in range(1,len(a[i]),2):
        s += 1
print(s)
