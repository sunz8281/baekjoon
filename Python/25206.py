d = ['F', ' ', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']

tot1 = 0
tot2 = 0
for _ in range(20):
    _, n, g = input().split()
    n = float(n)
    if g=='P': continue
    tot1 += n*d.index(g)*0.5
    tot2 += n

print(tot1/tot2)