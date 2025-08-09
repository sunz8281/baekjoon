n = int(input())
lst = [['*']*n for _ in range(n)]

def f(x, y, m):
    for i in range(m):
        for j in range(m):
            lst[x+m+i][y+m+j] = ' '
    if m==1: return
    for i in range(3):
        for j in range(3):
            f(x+(i*m), y+(j*m), m//3)


f(0, 0, n//3)
for i in range(n):
    print(''.join(lst[i]))