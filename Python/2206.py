from collections import deque
from copy import deepcopy

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

n, m = map(int, input().split())
nmmap = [list(map(int, input())) for _ in range(n)]

def bfs():
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    while queue:
        x, y, broken = queue.popleft()

        if x==n-1 and y==m-1:
            return visited[x][y][broken]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<n and 0<=ny<m): continue
            if nmmap[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                visited[nx][ny][broken] = visited[x][y][broken] + 1
                queue.append((nx, ny, broken))
            elif nmmap[nx][ny] == 1 and broken == 0:
                visited[nx][ny][1] = visited[x][y][broken] + 1
                queue.append((nx, ny, 1))
    return -1

print(bfs())