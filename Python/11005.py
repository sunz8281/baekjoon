n, b = map(int, input().split())

res = ''
while n>0:
    x = n%b
    n = n//b
    if x>=10:
        x = chr(x+55)
    res = str(x) + res
print(res.lstrip('0'))