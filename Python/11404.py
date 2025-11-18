import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = float('inf')

def dijkstra(start):
    q = [(0, start)]
    dist = [INF] * (n+1)
    dist[start] = 0
    while q:
        step, start = heapq.heappop(q)
        if dist[start] < step: continue
        for new_end, new_step in graph[start]:
            new_step = dist[start] + new_step
            if dist[new_end] <= new_step: continue
            dist[new_end] = new_step
            heapq.heappush(q, (new_step, new_end))
    return dist
for i in range(1, n+1):
    dist = list(map(lambda x: 0 if x==INF else x, dijkstra(i)))
    print(*dist[1:])