for m in map(int, [*open(0)][1].split()):
    if m == 300: l = 1
    elif m >= 275: l = 2
    elif m >= 250: l = 3
    else: l = 4
    print(l, end=' ')