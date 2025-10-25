n, r, c = map(int, input().split())
x = 2**n
result = 0
while x>1:
    x//=2
    if r>=x:
        result += x**2*2
        r-=x
    if c>=x:
        result += x**2
        c-=x
print(result)