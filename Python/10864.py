n, m = map(int, input().split())
lst = [[False]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    lst[a - 1][b - 1] = True
    lst[b - 1][a - 1] = True

for i in range(n):
    print(lst[i].count(True))