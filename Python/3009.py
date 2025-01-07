lstX = []
lstY = []
for _ in range(3):
    x, y = map(int, input().split())
    lstX.append(x)
    lstY.append(y)

print(2 * sum(set(lstX)) - sum(lstX), 2 * sum(set(lstY)) - sum(lstY))