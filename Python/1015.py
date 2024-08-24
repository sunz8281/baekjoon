n = int(input())
arr = list(map(int, input().split()))

sort_arr = sorted(arr)
P = []
for i in range(n):
    print(sort_arr.index(arr[i]), end=' ')
    sort_arr[sort_arr.index(arr[i])] -= 1