'''
Побудувати масив А=(ai), елементи якого задаються формулою:
a_i = (sin x + cos x)+2(sin 2x + cos 2x)+...+i(sin ix + cos ix), (i= 1,2,...,n)
Знайти найбільший елемент масиву А.
'''
from math import*
A = []
i = 1
a_i = 0
x = float(input('Please write x :  '))
n = int(input('Please write n :  '))
for i in range (1,n+1):
    a_i = n*(sin(n*x)) + n*(cos(n*x))
    A.append(a_i)
print(A)