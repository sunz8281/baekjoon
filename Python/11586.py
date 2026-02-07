n = int(input())
mirror = [list(input())for _ in range(n)]
k = int(input())
if k == 2:
    new_mirror = [[mirror[i][n-j-1]for j in range(n)]for i in range(n)]
elif k == 3:
    new_mirror = [[mirror[n-i-1][j] for j in range(n)]for i in range(n)]
else: new_mirror = mirror

for i in range(n):
    print(''.join(new_mirror[i]))