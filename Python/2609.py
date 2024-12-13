n, m = map(int, input().split())
x, y = n, m
while y!=0:
    t = x%y
    x = y
    y = t
print(x)
print(n*m//x)