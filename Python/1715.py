import heapq

n = int(input())
lst = [int(input()) for _ in range(n)]
heapq.heapify(lst)

result = 0
while len(lst) > 1:
    x, y = heapq.heappop(lst), heapq.heappop(lst)
    result += x+y
    heapq.heappush(lst, x+y)
print(result)