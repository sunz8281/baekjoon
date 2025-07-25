for _ in range(int(input())):
    c, p = map(int, input().split())
    print(c, p)
    print(p*1 + (p-2)*(c-1))