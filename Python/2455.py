p = 0
mx = 0
for _ in range(4):
    a, b = map(int, input().split())
    p += b-a
    mx = max(mx, p)
print(mx)