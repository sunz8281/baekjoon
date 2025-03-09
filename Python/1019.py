cnt = [0] * 10
i = 1
add = 0
n = int(input())
while n:
    x = n%10
    n//=10
    cnt[0] -= i
    for j in range(x):
        cnt[j] += (n+1)*i
    cnt[x] += n*i + add+1
    for j in range(x+1, 10):
        cnt[j] += n*i
    add += x*i
    i*=10
print(*cnt)