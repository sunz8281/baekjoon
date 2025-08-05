n, k = map(int, input().split())
lst = [[0]*6 for _ in range(2)]

for _ in range(n):
    s, y = map(int, input().split())
    lst[s][y-1] += 1

res = 0
for i in range(2):
    for j in range(6):
        res += (lst[i][j]+k-1)//k

print(res)