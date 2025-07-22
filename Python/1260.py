n, m, v = map(int, input().split())

link = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

dfs_is_visited = [False for _ in range(n+1)]
def dfs(x):
    dfs_is_visited[x] = True
    print(x, end=' ')
    for node in sorted(link[x]):
        if dfs_is_visited[node]: continue
        dfs(node)

bfs_is_visited = [False for _ in range(n+1)]
def bfs(x):
    l = [v]
    while l:
        node = l.pop(0)
        if bfs_is_visited[node]: continue
        bfs_is_visited[node] = True
        print(node, end=' ')
        l += sorted(link[node])

dfs(v)
print()
bfs(v)
