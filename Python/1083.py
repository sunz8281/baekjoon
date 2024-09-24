n = int(input())
arr = list(map(int, input().split()))
s = int(input())

sortArr = sorted(arr, reverse=True)
for i in range(n):
    for j in range(n):
        if sortArr[j] == -1 : continue
        idx = arr.index(sortArr[j])
        if idx-i <= s:
            sortArr[j] = -1
            s-= idx-i
            arr.insert(i, arr[idx])
            arr.pop(idx+1)
            break
    if s==0: break
    if sortArr == arr: break
print(*arr)