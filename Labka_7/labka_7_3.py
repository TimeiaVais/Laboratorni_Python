'''
Нехай x_0 = 0, x_1 = x_2 = x_3 = 7, x_i = (x_i_1*(1 + x_i_2) + x_i_3) / x_i_4.
Знайти x_n
'''
x_0 = 0
x_1 = x_2 = x_3 = 7
x_i_1 = 0
x_i_2 = 7
x_i_3 = 7
x_i_4 = 7
x_i = 0
n = int(input('Please write n : '))
i = int(input('Please write i : '))
def x_n(n):
    global x_0
    global x_1
    global x_2
    global x_3
    global x_i
    global x_i_1
    global x_i_2
    global x_i_3
    global x_i_4
    global i
    if n == 0:
        return 0
    elif n == 1:
        return 7
    elif n == 2:
        return 7
    elif n == 3:
        return 7
    elif n == i :
        return x_i == (x_i_1*(1 + x_i_2) + x_i_3) / x_i_4
    else:
        x_i_1 = 0
        x_i_2 = 7
        x_i_3 = 7
        x_i_4 = 7
        for i in range(n - 1, n):
             return (x_i_1*(1 + x_i_2) + x_i_3) / x_i_4
Xn = x_n(n)
print(Xn)