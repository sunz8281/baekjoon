n = int(input())
lst = sorted(list(map(int, input().split())))
result = 0
for i in range(n):
    result += sum(lst[:i+1])
print(result)