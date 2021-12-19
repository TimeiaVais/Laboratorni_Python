#Перевірити справедливість рівності при заданій точності: e**x = 1+x/factorial(1)+x**2/factorial(2)+...+x**n/factorial(n)+...
from math import*
'''
p - спепінь
fact - числа факторіалу
s - перший доданок 
'''
eps = float(input('Напишіть до якої точності обрахувати: '))
x = float(input('Please write x: '))
n = int(input('Please write n: '))
s = 1
from math import*
e = e

fact = 1
for num in range(2,n+1):
    fact *= num

p = 1
for num in range(2,n+1):
    p += num

for i in range(n):
    e = s + x**p/fact
    p += num
    fact *= num
while e < eps:
    e = s + x**p/fact
print('e**x = {0}'.format(e))



