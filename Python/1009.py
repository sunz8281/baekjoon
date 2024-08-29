t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(((a**((b-1)%4+1))-1)%10+1)

# 2 4 8 6 2
# 3 9 7 1 3
# 4 6 4 6 4
# 5 5 5 5 5
# 6 6 6 6 6
# 7 9 3 1 7