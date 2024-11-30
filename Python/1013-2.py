from re import compile
for _ in range(int(input())):
    s = input()
    if compile('(100+1+|01)+').fullmatch(s):
        print('YES')
    else:
        print('NO')
