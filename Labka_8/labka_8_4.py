#Розмістити елементи  діагоналі матриці у порядку спадання.
a = [#0 1  2
    [1, 2, 3], #0
    [6, 8, 1], #1
    [5, 7, 9]  #2
]
for i in range(len(a)):
    for j in range(len(a[i])):
        a.sort(reverse = True)
print(*a, sep = '\n')