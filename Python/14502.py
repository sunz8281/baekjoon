from collections import deque
from itertools import combinations

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(n)]

virus = []
empty = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            virus.append((i, j))
        elif lst[i][j] == 0:
            empty.append((i, j))

mx = 0
for items in combinations(empty, 3):
    virus_copy = deque(virus)
    lst_copy = [row[:] for row in lst]
    for item in items:
        lst_copy[item[0]][item[1]] = 1
    while virus_copy:
        i, j = virus_copy.popleft()
        for k in range(4):
            if 0<=i+dx[k]<n and 0<=j+dy[k]<m and lst_copy[i+dx[k]][j+dy[k]] == 0:
                virus_copy.append((i+dx[k], j+dy[k]))
                lst_copy[i+dx[k]][j+dy[k]] = 2
    mx = max(mx, sum(lst_copy[i].count(0) for i in range(n)))
print(mx)

