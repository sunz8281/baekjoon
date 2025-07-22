from collections import deque

n = int(input())

lst = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

visited = [False] * (n+1)
res = [0] * (n+1)
q = deque([1])
while q:
    x = q.popleft()
    visited[x] = True
    for y in lst[x]:
        if not visited[y]:
            res[y] = x
            q.append(y)
print('\n'.join(map(str, res[2:])))