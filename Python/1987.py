alpha = [0] * 26

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

def dfs(x, y):
    if x < 0 or x >= r or y < 0 or y >= c: return 0
    alpha_ord = ord(board[x][y]) - ord('A')
    if alpha[alpha_ord]: return 0
    alpha[alpha_ord] = 1
    mx = 0
    for i in range(4):
        mx = max(mx, dfs(x + dx[i], y + dy[i]))
    alpha[alpha_ord] = 0
    return mx + 1


print(dfs(0, 0))