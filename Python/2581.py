m = int(input())
n = int(input())
arr = [0]*(n+1)
arr[1] = 1
for i in range(2, n+1):
    if arr[i]: continue
    for j in range(i+i, n+1, i):
        arr[j] = 1

num = [i for i in range(m, n+1) if arr[i]==0]
if len(num):
    print(sum(num))
    print(min(num))
else:
    print(-1)