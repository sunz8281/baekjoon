from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(map(int, list(input()))))

lst[0][0] = 2
q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    if (x, y) == (n-1, m-1): break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == 1:
            q.append((nx, ny))
            lst[nx][ny] = lst[x][y] + 1

print(lst[n-1][m-1] - 1)