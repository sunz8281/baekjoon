minX = minY = 10000
maxX = maxY = -10000
for _ in range(int(input())):
    a, b = map(int, input().split())
    minX, maxX = min(minX, a), max(maxX, a)
    minY, maxY = min(minY, b), max(maxY, b)
print((maxX-minX)*(maxY-minY))