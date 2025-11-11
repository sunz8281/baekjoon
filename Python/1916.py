import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

q = [(0, start)]
INF = float('inf')
dist = [INF] * (n+1)
dist[start] = 0

while q:
    cost, node = heapq.heappop(q)
    if dist[node] < cost:
        continue
    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(q, (new_cost, next_node))
print(dist[end])
