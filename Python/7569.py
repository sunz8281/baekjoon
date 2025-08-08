from collections import deque

dx, dy, dz = [0, 0, 0, 0, -1, 1], [0, 0, -1, 1, 0, 0], [-1, 1, 0, 0, 0, 0]
m, n, h = map(int, input().split())
lst = []
q = deque([])
for i in range(h):
    lst.append([])
    for j in range(n):
        lst[-1].append(list(map(int, input().split())))
        for k in range(m):
            if lst[i][j][k] == 1: q.append((i, j, k))

def bfs():
    while q:
        x, y, z = q.popleft()
        for d in range(6):
            nx, ny, nz = x + dx[d], y + dy[d], z + dz[d]
            if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                if lst[nx][ny][nz] != 0: continue
                lst[nx][ny][nz] = lst[x][y][z] + 1
                q.append((nx, ny, nz))

bfs()
mx = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if lst[i][j][k] == 0:
                print(-1)
                exit(0)
            if lst[i][j][k] > mx: mx = lst[i][j][k]
print(mx - 1)