'''
Дано матрицю A. Звести дану матрицю до нижньої трикутної матриці.
'''
a =[ #0 1  2  3
    [1, 2, 3, 4],
    [5, 8, 4, 2],
    [5, 7, 2, 9],
    [5, 7, 3, 8]
]
for i in range(len(a)):
    for j in range(len(a[i])):
        if j>i:
            a[i][j] = 0
print(*a, sep ='\n')