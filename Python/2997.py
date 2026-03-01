a, b, c = sorted(map(int, input().split()))
x = min(c-b, b-a)
print(a+x if a+x!=b else b+x if b+x!=c else c+x)