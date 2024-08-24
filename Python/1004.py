def f(x1, x2, y1, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


t = int(input())

for _ in range(t):
    startX, startY, endX, endY = map(int, input().split())
    cnt = 0
    n = int(input())
    for i in range(n):
        x, y, r = map(int, input().split())
        start = f(x, startX, y, startY)
        end = f(x, endX, y, endY)
        if (r ** 2 < start and r ** 2 < end) or (r ** 2 > start and r ** 2 > end):
            continue
        else: cnt+=1
    print(cnt)