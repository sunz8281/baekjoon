n, m = map(int, input().split())
X = []
Y = []
for _ in range(m):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
x = min(X)
y = min(Y)

print(min(y*n, n//6*x+(n%6)*y, (n//6+((n%6+5)//6))*x))