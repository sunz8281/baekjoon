n = int(input())
for i in range(1, n):
    if sum(map(int, list(str(i))))+i == n:
        print(i)
        exit(0)
print(0)
