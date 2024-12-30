import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
tasks = [list(map(int, input().split()))[1:] for _ in range(n)]
works = [-1] * (m+1)

def dfs(k):
    for i in tasks[k]:
        if not visited[i] and works[i]!=k:
            visited[i] = True
            if works[i] == -1 or dfs(works[i]):
                works[i] = k
                return True
    return False

result = 0
for i in range(n):
    visited = [False] * (m+1)
    if dfs(i):
        result += 1
        if dfs(i):
            result += 1

print(result)