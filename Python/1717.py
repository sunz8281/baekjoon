import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
lst = [i for i in range(n+1)]

def root(x):
    if lst[x] == x:
        return x
    lst[x] = root(lst[x])
    return lst[x]

for i in range(m):
    x, a, b = map(int, input().split())
    if x==0:
        lst[root(a)] = root(b)
    else:
        print("YES" if root(a) == root(b) else "NO")