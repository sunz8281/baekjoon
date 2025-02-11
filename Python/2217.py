n = int(input())
lst = sorted([int(input()) for _ in range(n)])

result = 0
for i in range(n):
    value = lst[i] * (n-i)
    result = max(result, value)
print(result)