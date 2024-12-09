n = int(input())
lst = []
lst2 = [[]for i in range(n)]
for i in range(n):
    lst.append(input())
    for j in range(i):
        if lst[j].startswith(lst[i]) or lst[i].startswith(lst[j]):
            lst2[j].append(i)
            lst2[i].append(j)

cnt = [len(i) for i in lst2]

while any(lst2):
    x = cnt.index(max(cnt))
    for i in lst2[x]:
        lst2[i].remove(x)
        cnt[i] -= 1
    cnt[x] = -1
    lst2[x] = []
print(cnt.count(0))