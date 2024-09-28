n, k = map(int, input().split())

cnt = 0
while bin(n).count('1') > k:
    x = 1 << bin(n)[::-1].index('1')
    n += x
    cnt += x

print(cnt)