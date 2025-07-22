from collections import deque

m, n = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == 0 :
            lst[nx][ny] = lst[x][y] + 1
            q.append([nx, ny])

res = 0
for i in lst:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)