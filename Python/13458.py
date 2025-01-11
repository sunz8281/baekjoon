n = int(input())
lst = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = n
for i in lst:
    x = (i-b)/c
    if x > 0:
        if x != int(x):
            cnt += int(x) + 1
        else:
            cnt += int(x)
print(cnt)