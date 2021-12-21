#Розмістити елементи  діагоналі матриці у порядку спадання.
def sortDiagonal(a,M,N):
    for i in range(M):
        sm = a[i][i]
        pos = i
        for j in range(i+1,N):
            if (sm < a[j][j]):
                sm = a[j][j]
                pos = j
        a[i][i], a[pos][pos] = a[pos][pos], a[i][i]
    for i in range(M):
        for j in range(N):
            print(a[i][j],end=" ")
        print()
a = [
    [4,2,1],
    [3,1,5],
    [8,9,12]
]
sortDiagonal(a,3,3)