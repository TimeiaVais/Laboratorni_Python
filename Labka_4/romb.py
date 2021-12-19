# Позначення
'''
x1,у1-координати вершини А - int
x2,у2-координати вершини В - int
x3,у3-координати вершини С - int
x4,у4-координати вершини D - int

'''
# Знаходження довжин векторів
import math
AB = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(AB)
BC = math.sqrt((x3-x2)**2+(y3-y2)**2)
print(BC)
CD = math.sqrt((x4-x3)**2+(y4-y3)**2)
print(CD)
AD = math.sqrt((x4-x1)**2+(y4-y1)**2)
print(AD)

# Чи є ромб?
AC = math.sqrt((x3-x1)**2+(y3-y1)**2)
print('a {0}'.format(AC))
a = math.pow(AC,2)
print('AB**2={0}'.format(a))
BD = math.sqrt((x4-x2)**2+(y4-y2)**2)
print('b{0}'.format(BD))
b = math.pow(BD,2)
print('BD**2={0}'.format(b))
AB = math.sqrt((x2-x1)**2+(y2-y1)**2)
print('c{0}'.format(AB))
c = math.pow(AB,2)
print('4*BD**2={0}'.format(c))


