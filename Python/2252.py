import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
cnt = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    cnt[b-1] += 1

q = deque([i for i in range(n) if cnt[i]==0])
while q:
    x = q.popleft()
    print(x+1, end=' ')
    for i in arr[x]:
        cnt[i]-=1
        if cnt[i]==0:
            q.append(i)
