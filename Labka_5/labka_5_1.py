# Дано a є R, n є N. Знайти 1/a + 1/(a(a+1))+ ... + 1/(a(a+1)...(a+n))
'''
a - float
n - int
s - перший доданок
'''
#Введення даних
a = float(input('Please write a: '))
n = int(input('Please write n: '))
#Присвоєння невідомим якогось значення
x = a
y = (a+1)
s = 1/a
for i in range(n):
  sum = s + 1/(x*y)
  x = x*y
  y += 1
  print('Сума = {0}'.format(sum))
