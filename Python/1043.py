n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[x] = y

def unions(x, *args):
    if len(args) == 0: return
    for arg in args:
        union(x, arg)

knowing = list(map(int, input().split()))[1:]

if knowing: unions(*knowing)

parties = []
for _ in range(m):
    parties.append(list(map(int, input().split()))[1:])
    unions(*parties[-1])

head = find(knowing[0]) if knowing else -1
cnt = 0
for party in parties:
    if find(party[0]) != head: cnt+=1
print(cnt)