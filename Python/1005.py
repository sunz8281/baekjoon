from collections import deque
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    times = list(map(int, sys.stdin.readline().split()))

    arr = [[] for i in range(n)]
    cnt = [0]*n
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[x-1].append(y-1)
        cnt[y-1] += 1

    queue = deque(i for i in range(n) if cnt[i]==0)
    dp = [i for i in times]

    while queue:
        current = queue.popleft()
        time = dp[current]

        for x in arr[current]:
            dp[x] = max(dp[x], time+times[x])
            cnt[x] -= 1
            if(cnt[x]==0):
                queue.append(x)

    w = int(sys.stdin.readline())
    print(dp[w-1])
