team = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
mx = 0
mxIdx = 0
_ = input()
for i in range(9):
    n = max(map(int, input().split()))
    if mx < n:
        mx = n
        mxIdx = i
print(team[mxIdx])