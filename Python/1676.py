re = 1
for i in range(1, int(input())+1):
    re *= i

cnt = 0
while re % 10 == 0:
    re //= 10
    cnt += 1
print(cnt)