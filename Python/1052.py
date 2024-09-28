n, k = map(int, input().split())

cnt=0
while list(str(bin(n))).count('1') > k:
    x = 1 << list(str(bin(n)))[::-1].index('1')
    n += x
    cnt+=x

print(cnt)