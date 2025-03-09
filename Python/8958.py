for _ in range(int(input())):
    lst = input()
    point = 0
    add = 0
    for c in lst:
        if c == 'O':
            point += 1 + add
            add += 1
        else: add = 0
    print(point)