n, _ = map(int, input().split())
lst = [4, 11, 23, 40, 60, 77, 89, 96, 100]
g = list(map(lambda x: int(x)*100//n, input().split()))
for i in g:
    for j in range(9):
        if i<=lst[j]:
            print(j+1, end=' ')
            break