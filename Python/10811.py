n, m = map(int, input().split())
arr = [i for i in range(0, n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a:b+1] = arr[b:a-1:-1]

print(*arr[1:])