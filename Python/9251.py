import sys
sys.setrecursionlimit(10000)

a = input()
b = input()

lenA = len(a)
lenB = len(b)

memo = [[-1]*lenB for _ in range(lenA)]
def lcs(x, y):
    if x>=lenA or y>=lenB: return 0
    if memo[x][y] != -1: return memo[x][y]

    if a[x] == b[y]: re = lcs(x+1, y+1) + 1
    else: re = max(lcs(x+1, y), lcs(x, y+1))
    memo[x][y] = re
    return re

print(lcs(0, 0))