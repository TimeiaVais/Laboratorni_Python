'''
Дано текстовий файл, який містить цілі числа. Визначити середнє арифметичне елементів.
'''
s = 0
with open('my.txt') as f:
   r = f.readlines()
   print(r)
   s = (int(r[0])+int(r[1])+int(r[2])+int(r[3])+int(r[4])+int(r[5]))/6
print(s)