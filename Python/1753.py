import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())-1

graph = [[] for _ in range(V)]
for _ in range(E):
    u, v, e = map(int, input().split())
    graph[u-1].append((v-1, e))

INF = 1e9
result = [INF]*V
q = [(0, k)]
while q:
    d, node = heapq.heappop(q)
    if d >= result[node]: continue
    result[node] = d
    for v, e in graph[node]:
        heapq.heappush(q, (d+e, v))

for item in result:
    if item == INF: print("INF")
    else: print(item)