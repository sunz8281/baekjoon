a, b, c = map(int, input().split())
result = 1
if a%2 or b%2 or c%2:
    if a%2: result *= a
    if b%2: result *= b
    if c%2: result *= c
else: result = a*b*c
print(result)