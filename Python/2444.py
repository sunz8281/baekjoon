n = int(input())
for i in range(1, n+1):
    print(" "*(n-i), end='')
    print("*"*(i*2-1))

for i in range(1, n):
    print(" "*i, end='')
    print("*"*(n*2-(i*2+1)))