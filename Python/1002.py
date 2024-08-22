def f(x1, y1, r1, x2, y2, r2):
    d = ((x1-x2)** 2 + (y1-y2)** 2)**(1/2)
    if d==0 and r1==r2:
        return -1
    
    elif d ==r1+r2 or d+r1==r2 or d+r2==r1:
        return 1
    
    elif d>r1+r2 or r2+d<r1 or r1+d<r2:
        return 0
    
    else: return 2

n = int(input())
for i in range(0, n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(f(x1, y1, r1, x2, y2, r2))