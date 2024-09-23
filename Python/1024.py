import sys

n, l = map(int, input().split())
for i in range(l, 101):
    start = n//i-((i-1)//2)
    if start < 0: continue
    arr = [j for j in range(start, start+i)]
    if sum(arr)==n:
        print(*arr)
        sys.exit(0)
print(-1)
