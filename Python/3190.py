from collections import deque

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)

n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]
board[0][0] = 1

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2

l = int(input())
direction = 0
path = deque([(0, 0)])
headX, headY = 0, 0
time = 0
for _ in range(l):
    x, c = input().split()
    for i in range(int(x)-time):
        headX, headY = headX + dx[direction], headY + dy[direction]
        if not(0<=headX<n and 0<=headY<n) or board[headX][headY] == 1:
            print(time+i+1)
            exit(0)
        if board[headX][headY] == 0:
            tailX, tailY = path.popleft()
            board[tailX][tailY] = 0
        board[headX][headY] = 1
        path.append((headX, headY))
    if c=='L':
        direction = (direction+3)%4
    else:
        direction = (direction+1)%4
    time = int(x)

while True:
    time+=1
    headX, headY = headX + dx[direction], headY + dy[direction]
    if not (0 <= headX < n and 0 <= headY < n) or board[headX][headY] == 1:
        print(time)
        break
    if board[headX][headY] == 0:
        tailX, tailY = path.popleft()
        board[tailX][tailY] = 0
    board[headX][headY] = 1
    path.append((headX, headY))