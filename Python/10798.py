arr = []
for _ in range(5):
    arr.append(list(input()))

check = [False, False, False, False, False]
while False in check:
    for i in range(len(arr)):
        if len(arr[i]) == 0:
            check[i] = True
            continue
        print(arr[i][0], end='')
        arr[i].pop(0)
