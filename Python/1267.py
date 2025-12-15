n = int(input())
lst = list(map(int, input().split()))
Y = 0
M = 0
for item in lst:
    Y += (item//30+1)*10
    M += (item//60+1)*15

if Y > M:
    print("M", M)
elif Y < M:
    print("Y", Y)
else: print("Y M", Y)