t, x = map(int, input().split())
n = int(input())

for i in range(n):
    k = int(input())
    lst = list(map(int, input().split()))
    if x not in lst:
        print("NO")
        exit(0)
print("YES")