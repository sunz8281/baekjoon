d = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
lst = [[0]*2001 for _ in range(2001)]
x, y = 1000, 1000
lst[x][y] = 1
n = int(input())
commands = list(input())
for command in commands:
    dx, dy = d[command]
    x, y = x + dx, y + dy
    lst[x][y] = 1
print(sum(lst[i].count(1) for i in range(2001)))