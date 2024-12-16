a, b, c = map(int, input().split())

if c<=b: print(-1)
else:
    x = a/(c-b)
    print(int(x+1))