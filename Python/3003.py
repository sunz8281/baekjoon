d = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
print(*[(d[i] - arr[i]) for i in range(6)])