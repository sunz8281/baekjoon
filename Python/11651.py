print(*sorted([*open(0)][1:], key=lambda x:(int(x.split()[1]), int(x.split()[0]))), sep='')