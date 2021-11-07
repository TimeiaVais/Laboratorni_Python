'''
Знайти вектор
c = 2(a +c)- b, де a,b,c належить R**n
'''
# Позначення
'''
n - кл-сть вимірів
a,b,c - вектори
m - результат
'''
m = []
n = int(input('n = '))
a = [float(input('Please write a_{0} ='.format(i))) for i in range(1, n+1)]
b = [float(input('Please write b_{0} ='.format(i))) for i in range(1, n+1)]
c = [float(input('Please write c_{0} ='.format(i))) for i in range(1, n+1)]
for i in range(n):
    c[i] = (2*(a[i] + c[i])) - b[i]
    m.append(c[i])
print('c = {0}'.format(m))