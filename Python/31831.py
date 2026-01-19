n, m = map(int, input().split())
lst = list(map(int, input().split()))
stress = 0
result = 0
for i in range(n):
    stress += lst[i]
    if stress < 0: stress = 0
    elif stress >= m: result += 1
print(result)