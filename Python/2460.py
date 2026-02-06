lst = [0]
for _ in range(10):
    x, y = map(int, input().split())
    lst.append(lst[-1]-x+y)
print(max(lst))