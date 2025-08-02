import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = [[]]
for _ in range(n):
    lst.append(list(map(int, input().split())))

memo = [[-1] * (k+1) for _ in range(n+1)]
def memoization(i, j):
    if i<=0 or j<=0: return 0
    if memo[i][j] == -1:
        w, v = lst[i]
        if j-w >= 0:
            memo[i][j] = max(memoization(i-1, j), memoization(i-1, j-w)+v)
        else:
            memo[i][j] = memoization(i-1, j)
    return memo[i][j]

print(memoization(n, k))