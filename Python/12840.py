h, m, s = map(int, input().split())
for _ in range(int(input())):
    T, *c = map(int, input().split())
    if T==1:
        s = h*3600+m*60+s + c[0]
    elif T==2:
        s = h*3600+m*60+s + 3600*24 - c[0]
    else:
        print(h, m, s)
        continue

    h, m, s = s // 3600 % 24, s % 3600 // 60, s % 60


