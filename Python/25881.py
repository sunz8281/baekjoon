n, m = map(int, input().split())
for _ in range(int(input())):
    x = int(input())
    print(x, min(x, 1000)*n+max(0, x-1000)*m)