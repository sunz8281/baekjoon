l = [13, 7, 5, 3, 3, 2]
c = list(map(int, input().split()))
h = list(map(int, input().split()))
print('cocjr0208' if sum([c[i]*l[i] for i in range(6)])>sum([h[i]*l[i] for i in range(6)])+1.5 else 'ekwoo')