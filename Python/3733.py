for l in [*open(0)]:
    n, s = map(int, l.split())
    print(s//(n+1))