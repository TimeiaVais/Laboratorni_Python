#Нехай x0 = x1 = 1, x_i = sin(x_i_1) + x_i_2/cos(x_i_1). Визначити х_n
x0 = x1 = 1
from math import*
x_i_1 = 1
x_i_2 = 1
n = int(input('Please write n: '))
for i in range(2,n+1):
    x_i = sin(x_i_1) + x_i_2/cos(x_i_1)
    x_i_1 = x_i_2
    x_i_2 = x_i_1
    x_i_1 = x_i
    print(x_i)
