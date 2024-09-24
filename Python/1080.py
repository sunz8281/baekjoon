n, m = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(list(map(int, list(input()))))
for _ in range(n):
    arr2.append(list(map(int, list(input()))))

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if arr1[i][j]==arr2[i][j]: continue
        cnt += 1
        for ii in range(i, i+3):
            for jj in range(j, j+3):
                # print(ii, jj)
                arr1[ii][jj] = not arr1[ii][jj]

if arr1 == arr2: print(cnt)
else: print(-1)