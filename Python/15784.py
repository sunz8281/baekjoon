n, a, b = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

a, b = a-1, b-1
pt = lst[a][b]
for i in range(n):
    if lst[a][i] > pt or lst[i][b] > pt:
        print('ANGRY')
        break
else:
    print('HAPPY')