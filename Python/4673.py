lst = [True]*10001
f = lambda x: x if x < 10 else x%10 + f(x//10)
for i in range(1, 10001):
    n = i + f(i)
    if n>10000: continue
    lst[n] = False

for i in range(1, 10001):
    if lst[i]: print(i)