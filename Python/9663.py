n = int(input())

vertical_blocked = [0]*n
diagonal_blocked1 = [0]*n*2
diagonal_blocked2 = [0]*n*2

def dfs(x):
    if x >= n: return 1
    cnt = 0
    for y in range(n):
        if not (vertical_blocked[y] or diagonal_blocked1[x+y] or diagonal_blocked2[x-y+n]):
            vertical_blocked[y], diagonal_blocked1[x+y], diagonal_blocked2[x-y+n] = 1, 1, 1
            cnt += dfs(x+1)
            vertical_blocked[y], diagonal_blocked1[x+y], diagonal_blocked2[x-y+n] = 0, 0, 0
    return cnt

print(dfs(0))