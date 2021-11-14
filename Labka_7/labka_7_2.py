'''
Дано послідовність натуральних числень a_1, a_2, ... , a_n . Використовуючи підпрограму, яка дозволяє
встановити, чи є послідовність із чотирьох чисел геометричною прогресією, знайти
кількість послідовно розміщених четвірок чисел, які утворюють геометричну прогресію.
'''
import random
n = int(input('n = '))
ans = input('1.From keyboard \n2.Random \nYour choice: ')
i = 1
if ans == '1':
    a = [int(input('Please write a_{0} : '.format(i))) for i in range (1, n + 1)]
else:
    a = [random.randint(1,100) for i in range (1, n + 1)]
print(a)

def geometric_progression(b):
    r = b[2] / b[1] and b[4] / b[3]
    if r == b[2]/b[1] and b[4]/b[3]:
        return r
q = a[2]/a[1] and a[4]/a[3]
if geometric_progression(a) == q:
    q = a[2]/a[1] and a[4]/a[3]
    print('Геометрична прогресія')
else:
    print('False')
