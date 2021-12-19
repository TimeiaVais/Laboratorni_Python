'''
Дано три дійсних числа:a,b,c .
Скласти програму для знаходження(min(a,b,c))**2 .
'''

#Позначення
'''
a = first_number   - float
b = second_number  - float
c = third_number   - float
min = minimum      - float
'''
#Введення даних
first_number = float(input('Введіть число №1: '))
second_number = float(input('Введіть число №2: '))
third_number = float(input('Введіть число №3: '))
min = 0
import math

#Порівняння
if first_number<second_number or first_number<third_number:
   print('min {0}'.format(first_number))
   m = math.pow(first_number, 2)
   print('квадрат мінімума ={0}'.format(m))
elif second_number<first_number or second_number<third_number:
   print('min {0}'.format(second_number))
   m = math.pow(second_number, 2)
   print('квадрат мінімума ={0}'.format(m))
elif third_number<first_number or third_number<second_number:
   print('min {0}'.format(third_number))
   m = math.pow(third_number, 2)
   print('квадрат мінімума ={0}'.format(m))

