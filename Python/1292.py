a, b = map(int, input().split())
num, cnt = 1, 0
for i in range(1, a):
    cnt += 1
    if num == cnt:
        cnt = 0
        num += 1

re = 0
for i in range(a, b+1):
    re += num
    cnt += 1
    if num == cnt:
        cnt = 0
        num += 1
print(re)