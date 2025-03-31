n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))

cnt = {}
for i in lst1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in lst2:
    print(cnt[i] if i in cnt else 0, end=' ')