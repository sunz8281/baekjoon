s = input()
l = [(s[i], s[i+1]) for i in range(0, len(s), 2)]
a, b = 0, 0

for x, p in l:
    if x=='A': a += int(p)
    else: b += int(p)
print('A' if a > b else 'B')