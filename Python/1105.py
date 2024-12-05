from collections import deque

l, r = map(deque, input().split())

if len(l) != len(r):
    print(0)
    exit(0)

count = 0
while l and r:
    x, y = l.popleft(), r.popleft()
    if x!=y: break
    if x=='8':
        count += 1
print(count)