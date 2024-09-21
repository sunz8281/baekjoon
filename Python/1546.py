n = int(input())
arr = list(map(int, input().split()))
arrMax = max(arr)
arr = [arr[i]/arrMax*100 for i in range(n)]
print(sum(arr)/n)