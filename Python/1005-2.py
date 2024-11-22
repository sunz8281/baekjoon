import sys
sys.setrecursionlimit(10**6)
def f(w, times, arr, memo):
    if memo[w] == -1:
        if len(arr[w]) == 0:
            memo[w] = times[w]
        else:
            memo[w] = times[w] + max(f(v, times, arr, memo) for v in arr[w])
    return memo[w]
    
T = int(sys.stdin.readline())
for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    times = list(map(int, sys.stdin.readline().split()))

    arr = [[] for i in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[y-1].append(x-1)

    w = int(sys.stdin.readline())
    memo = [-1]*n
    print(f(w-1, times, arr, memo))
