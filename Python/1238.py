import heapq

n, m, x = map(int, input().split())
road = [[] for _ in range(n)]
rev_road = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    road[a-1].append((t, b-1))
    rev_road[b-1].append((t, a-1))

INF = float('inf')
def dijkstra(start, graph):
    q = [(0, start)]
    dist = [INF] * n
    dist[start] = 0
    while q:
        cost, destination = heapq.heappop(q)
        if dist[destination] < cost: continue
        for new_cost, new_dest in graph[destination]:
            if cost + new_cost < dist[new_dest]:
                new_cost = cost + new_cost
                dist[new_dest] = new_cost
                heapq.heappush(q, (new_cost, new_dest))
    return dist

go = dijkstra(x-1, road)
back = dijkstra(x-1, rev_road)
hap = [go[i] + back[i] for i in range(n)]
print(max(hap))