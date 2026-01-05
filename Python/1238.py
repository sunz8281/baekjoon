import heapq

n, m, x = map(int, input().split())
road = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    road[a-1].append((t, b-1))

def bfs(start, end):
    q = [(0, start)]
    dist = [INF] * n
    dist[start] = 0
    while q:
        cost, destination = heapq.heappop(q)
        if dist[destination] < cost: continue
        dist[destination] = cost
        if destination == end: break
        for new in road[destination]:
            new_cost, new_dest = new
            if cost + new_cost < dist[new_dest]:
                heapq.heappush(q, (cost + new_cost, new_dest))
    return dist[end]

INF = float('inf')
result = [0] * n
for i in range(n):
    result[i] = bfs(i, x-1) + bfs(x-1, i)
print(max(result))