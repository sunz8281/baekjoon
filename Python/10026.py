import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
lst = [list(input()) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

q = deque()
def bfs(x, y, alpha):
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if x < 0 or x >= n or y < 0 or y >= n: continue
        if visited[x][y]: continue
        if lst[x][y] != alpha: continue
        visited[x][y] = True
        for k in range(4):
            q.append((x + dx[k], y + dy[k]))


cnt1 = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt1 += 1
            bfs(i, j, lst[i][j])


for i in range(n):
    for j in range(n):
        if lst[i][j] == 'R': lst[i][j] = 'G'


cnt2 = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt2 += 1
            bfs(i, j, lst[i][j])

print(cnt1, cnt2)