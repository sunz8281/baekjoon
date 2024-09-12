x = int(input())
cnt = 0

while x:
    cnt += x%2
    x //= 2
print(cnt)

