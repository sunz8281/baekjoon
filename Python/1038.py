from itertools import combinations

n = int(input())

lst = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(map(str, j[::-1]))
        lst.append(int(num))

lst.sort()
try:
    print(lst[n])
except:
    print(-1)