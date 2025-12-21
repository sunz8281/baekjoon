from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
INF = float('inf')

n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))
    for j in range(n):
        if lst[i][j]== 9:
            s_x, s_y = i, j
            lst[i][j] = 0

shark = 2
turn = 0
eat_count = 0
while True:
    space = [[-1] * n for _ in range(n)]
    space[s_x][s_y] = 0
    q = deque([(s_x, s_y)])
    fish = (INF, INF, INF)
    while q:
        x, y = q.popleft()
        cost = space[x][y]
        if 0 != lst[x][y] < shark: fish = min(fish, (cost, x, y))
        if cost >= fish[0]: continue
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if (nx < 0 or nx >= n or ny < 0 or ny >= n
                    or lst[nx][ny] > shark
                    or space[nx][ny] != -1):
                continue
            q.append((nx, ny))
            space[nx][ny] = cost+1

    if fish[0] >= INF:
        break
    fish_cost, fish_x, fish_y = fish
    turn += fish_cost
    lst[fish_x][fish_y] = 0
    s_x, s_y = fish_x, fish_y
    eat_count += 1
    if eat_count == shark:
        shark += 1
        eat_count = 0
print(turn)