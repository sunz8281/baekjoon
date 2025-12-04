import heapq

n, k = map(int, input().split())
q = [(0, n)]
mx = max(n, k)
dist = [float('inf')] * (mx*2)
while q:
    x, y = heapq.heappop(q)
    if dist[y] <= x: continue
    dist[y] = x
    if y < mx:
        if dist[y*2] > x:
            heapq.heappush(q, (x, y*2))
        if dist[y+1] > x+1:
            heapq.heappush(q, (x+1, y+1))
    if y > 0 and dist[y-1] > x+1:
        heapq.heappush(q, (x+1, y-1))
print(dist[k])