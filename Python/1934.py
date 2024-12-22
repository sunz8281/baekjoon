f = lambda a, b: a if b==0 else f(b, a%b)
for _ in range(int(input())):
    a, b = map(int, input().split())
    print((a*b)//f(a, b))