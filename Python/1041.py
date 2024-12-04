n = int(input())
lst = list(map(int, input().split()))
if n==1:
    print(sum(lst)-max(lst))
    exit(0)

lst2 = []
for i in range(3):
    lst2.append(min(lst[i], lst[5-i]))

total = 0
total += min(lst) * ((n-2)*4*(n-1) + ((n-2)**2))
total += (sum(lst2) - max(lst2)) * ((n*2 + -3)*4)
total += sum(lst2) * 4
print(total)