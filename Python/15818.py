n, m = map(int, input().split())
result = 1
for i in map(int, input().split()):
    result = (result*i)%m
print(result)