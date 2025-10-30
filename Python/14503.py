dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

x, y = r, c
cnt = 0
while True:
    if room[x][y] == 0:
        cnt += 1
        room[x][y] = -1

    for _ in range(4):
        d = (d+3)%4
        nx, ny = x + dx[d], y + dy[d]
        if room[nx][ny] == 0:
            x, y = nx, ny
            break
    else:
        nd = (d+2)%4
        nx, ny = x + dx[nd], y + dy[nd]
        if room[nx][ny] != 1:
            x, y = nx, ny
        else:
            break
print(cnt)

