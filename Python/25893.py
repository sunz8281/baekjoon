for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(a, b, c)
    a, b, c = sorted((a, b, c))
    if c < 10: print('zilch')
    elif b < 10: print('double')
    elif a < 10: print('double-double')
    else: print('triple-double')
    print()
