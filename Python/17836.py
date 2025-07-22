from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m, t = map(int, input().split())

lst = []
for i in range(n):
    line = list(map(int, input().split()))
    lst.append(line)
    if 2 in line:
        a, b = i, line.index(2)
        lst[a][b] = 'x'

q = deque([(0, 0)])
lst[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and (lst[nx][ny] == 0 or lst[nx][ny] == 'x'):
            lst[nx][ny] = lst[x][y] + 1
            q.append((nx, ny))

if lst[n-1][m-1] and lst[a][b]!='x' : res = min(lst[n-1][m-1], lst[a][b]+abs(n-1-a)+abs(m-1-b))
elif lst[n-1][m-1]: res = lst[n-1][m-1]
elif lst[a][b]!='x': res = lst[a][b]+abs(n-1-a)+abs(m-1-b)
else: res = t + 2
res -= 1

if res<=t: print(res)
else: print('Fail')
