def dfs(depth, idx):
    if depth == 6:
        print(*result)
        return
    for i in range(idx, k):
        result.append(S[i])
        dfs(depth + 1, i + 1)
        result.pop()

while True:
    k, *S = map(int, input().split())
    if k == 0: break
    result = []
    dfs(0, 0)
    print()
