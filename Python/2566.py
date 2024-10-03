arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))

x, y = 0, 0
for i in range(9):
    m = max(arr[i])
    if arr[x][y] < m:
        x, y = i, arr[i].index(m)

print(arr[x][y])
print(x+1, y+1)