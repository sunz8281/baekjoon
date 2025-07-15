n = int(input())
lst = [i+1 for i in range(n)]
for i in map(int, input().split()):
    lst.remove(i)
print(lst[0])
