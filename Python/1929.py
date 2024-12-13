m, n = map(int, input().split())
lst = [False] * (n+1)
for i in range(2, n+1):
    if lst[i]: continue
    if i>=m: print(i)
    for j in range(i*i, n+1, i):
        lst[j] = True