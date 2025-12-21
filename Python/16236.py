from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

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
    q = deque([(0, s_x, s_y)])
    fish = (1000000, )
    while q:
        cost, x, y = q.popleft()
        if space[x][y] != -1 and space[x][y] <= cost: continue
        if 0 != lst[x][y] < shark: fish = min(fish, (cost, x, y))
        space[x][y] = cost
        if cost >= fish[0]: continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or lst[x][y] > shark: continue
            q.append((cost+1, nx, ny))

    if fish == (1000000, ):
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