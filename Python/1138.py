n = int(input())
lst = list(map(int, input().split()))

result = [0] * n
for i in range(n):
    x = -1
    for _ in range(lst[i]+1):
        x+=1
        while result[x]: x+=1
    result[x] = i+1

print(*result)