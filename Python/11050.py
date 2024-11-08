n, k = map(int, input().split())

arr = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(min(i, k)+1):
        if i==j or j==0: x=1
        elif j==1: x=i
        else: x=arr[i-1][j-1]+arr[i-1][j]
        arr[i][j] = x
print(arr[n][k])