n = int(input())
for i in range(n//5, -1, -1):
    x = n - (5*i)
    if x%3 == 0:
        print(i + x//3)
        exit(0)

print(-1)