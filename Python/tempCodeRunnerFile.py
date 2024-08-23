import sys
sys.setrecursionlimit(10**7)
def g(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

def f(r, n):
    sum = g(n)
    if(r==1): return 1
    if(sum>r-n): return f(r-n, n-1)+1
    if(sum==r): return f(r-n, n)+1
    if(sum+n>=r-n): return f(r-n, n)+1
    return f(r-n, n+1)+1

t  = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(f(y-x, 1))