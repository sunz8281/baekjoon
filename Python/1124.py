a, b = map(int, input().split())

lst = [0]*(b+1)
lst2 = []
# 에라토스테네스의 체
for i in range(2, b+1):
    if lst[i]: continue
    lst2.append(i)
    for j in range(i*i, b+1, i):
        lst[j] = 1

# 소인수 소수 판별
result = 0
for i in range(a, b+1):
    cnt = 0
    x = i
    for j in lst2:
        if j * j > i: break
        while x % j == 0:
            cnt += 1
            x //= j
    if x>1: cnt+=1
    if cnt in lst2:
        result += 1
print(result)
