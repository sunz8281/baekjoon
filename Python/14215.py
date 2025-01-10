a, b, c = sorted(map(int, input().split()))
c = min(a + b - 1, c)
print(a + b + c)