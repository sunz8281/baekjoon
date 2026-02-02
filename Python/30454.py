n, l = map(int, input().split())
mx = 0
same = 0
for i in range(n):
    horse = list(map(int, input()))
    cnt = horse[0]
    for j in range(l-1):
        if horse[j]==0 and horse[j+1]==1:
            cnt += 1
    if mx == cnt: same += 1
    elif mx < cnt:
        mx = cnt
        same = 1
print(mx, same)