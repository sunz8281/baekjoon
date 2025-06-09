lst = []
for _ in range(5):
    n = int(input())
    if n in lst: lst.remove(n)
    else: lst.append(n)
print(lst[0])