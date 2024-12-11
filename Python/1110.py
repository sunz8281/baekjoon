def f(k):
    return (k % 10) * 10 + (k // 10 + k % 10) % 10

n = int(input())
cnt = 1
x = f(n)
while x != n:
    cnt+=1
    x = f(x)
print(cnt)