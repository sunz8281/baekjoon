a, b = map(int, input().split())
lst = list(map(int, input().split()))
for i in lst:
    print(i-a*b, end=' ')