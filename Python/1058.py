N = int(input())
arr = []
max = 0

for _ in range(N):
    arr.append(list(input()))

for i in range(N):
    friend = [0]*N
    for j in range(N):
        if arr[i][j]=='N': continue
        friend[j] = 1
        for k in range(N):
            if i==k: continue
            if arr[j][k]=='N': continue
            friend[k] = 1
            
    cnt = friend.count(1)
    if max<cnt: max=cnt
print(max)