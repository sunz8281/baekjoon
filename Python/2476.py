result = 0
for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    point = 0
    if a==b==c: point = 10000+1000*a
    elif a==b or b==c: point = 1000+100*b
    else: point = 100*c
    result = max(result, point)
print(result)