'''
Дано нетипізований файл, який містить цілі числа. Створити файл «P1.dat»,
який містить парні цілі числа. Непарні числа вивести на екран у порядку,
зворотному до порядку слідування їх у файлі.
'''
with open('my.txt') as f:
    with open('P1.dat.txt', 'w') as f_dat:
        with open('odd_nums.txt', 'w') as f_odd:
            for num in f:
                n = int(num)
                if n % 2 == 0:
                    f_dat.write(str(n) + '\n')
                else:
                    f_odd.write(str(n) + '\n')