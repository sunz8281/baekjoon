m = int(input())
n = int(input())
lst = []
for i in range(m, n+1):
    if i**0.5 == int(i**0.5):
        lst.append(i)
if lst:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)