N, a, b = map(int, input().split())
cnt=0

while 1:
    cnt+=1
    a =(a+1)//2
    b =(b+1)//2
    if a==b: break

print(cnt)

# 1 2 3 4
#  1   2
#    1

# 1 2 3 4 5 6
#  1   2   3
#    1     2
#       1

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
#  1   2   3   4   5     6     7     8
