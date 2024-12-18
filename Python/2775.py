memo = [[0]*15 if i!=0 else [j for j in range(15)] for i in range(15)]
def f(a, b):
    if memo[a][b] == 0:
        memo[a][b] = sum([f(a-1, i) for i in range(1, b+1)])
    return memo[a][b]

for i in range(int(input())):
    k, n = int(input()), int(input())
    print(f(k, n))