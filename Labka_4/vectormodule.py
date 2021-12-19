from math import*

# ВВедення позначень
'''
a - довжина вектора А - int
b - довжина вектора В - int
c - довжина вектора С - int
p - периметр          - int
sqrt - корінь квадратний - int
x1,y1 - координати А  - int
x2,y2 - координати В  - int
x3,y3 - координати С  - int
'''
# ВВедення даних
x1 = int(input('Введіть x1: '))
y1 = int(input('Введіть y1: '))
x2 = int(input('Введіть x2: '))
y2 = int(input('Введіть y2: '))
x3 = int(input('Введіть x3: '))
y3 = int(input('Введіть y3: '))

# Знаходження довжин векторів
a = int(sqrt((x2-x1)**2+(y2-y1)**2))
print('Значення a = {0}'.format(a))
b = int(sqrt((x3-x2)**2+(y3-y2)**2))
print('Значення b = {0}'.format(b))
c = int(sqrt((x3-x1)**2+(y3-y1)**2))
print('Значення c = {0}'.format(c))
#Знаходження периметру
p = a+b+c
print('Значення p = {0}'.format(p))


