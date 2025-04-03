n, k = map(int, input().split())

lst = [i for i in range(1, n+1)]
idx = 0

res = []
for i in range(n):
    idx = (idx+k-1)%(n-i)
    res.append(lst.pop(idx))

print('<'+', '.join(map(str, res)) +'>')
