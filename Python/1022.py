y1, x1, y2, x2 = map(int, input().split())

def g(n):
    if(n<10): return 1
    return g(n//10) + 1

def f(y, x):
    maxxy = max(abs(x), abs(y))
    turn = maxxy+1
    if turn == 1: return 1
    avg = ((turn + maxxy) ** 2) - ( maxxy *2 *2)
    if x > y: 
        if x==maxxy: return avg - maxxy * 2 - (x+y)
        else: return avg - (x-y)
    else:
        if y==maxxy: return avg + maxxy * 2 + (x+y)
        else: return avg - (x-y)


num = max(f(y1, x1), f(y1, x2), f(y2, x1), f(y2, x2))
num = g(num)

for i in range(y1, y2+1):
    for j in range(x1, x2+1):
        print("%*d" %(num, f(i, j)), end=' ')
    print()

# 2 1 -> -7
# 2 0 -> -6 
# 2 -1 -> -5 
# 2 -2 -> -4 
# x>y avg - maxxy * 2 - (x+y)

# 1 -2 -> -3
# 0 -2 -> -2
# -1 -2 -> -1
# x>y avg - (x-y)

# -2 -2 -> 0
# -2 -1 -> 1
# -2 0 -> 2
# -2 1 -> 3
# x<=y avg - (x-y)

# -2 2 -> 4
# -1 2 -> 5
# 0 2 -> 6
# 1 2 -> 7
# 2 2 -> 8
#x<=y avg + maxxy * 2 + (x+y)