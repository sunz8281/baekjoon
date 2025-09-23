n = int(input())
mxidx = 0
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
    if lst[mxidx][0] < lst[i][0]: mxidx = i
    elif lst[mxidx][0] == lst[i][0]:
        if lst[mxidx][1] > lst[i][1]: mxidx = i
        elif lst[mxidx][1] == lst[i][1]:
            if lst[mxidx][2] > lst[i][2]: mxidx = i
print(mxidx+1)
