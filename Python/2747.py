def f(k):
    if not memo[k] : memo[k] = f(k-1) + f(k-2)
    return memo[k]

n = int(input())
memo = [0]*46
memo[1], memo[2] = 1, 1
print(f(n))