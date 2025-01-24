import sys
input = sys.stdin.readline

n = int(input())
lst = []
dic = {}
for _ in range(n):
    lst.append(int(input()))
    if lst[-1] not in dic.keys():
        dic[lst[-1]] = 0
    dic[lst[-1]] += 1
dic = sorted(dic.items(), key=lambda x: (x[1], -x[0]), reverse=True)
print(round(sum(lst)/n))
print(sorted(lst)[n//2])
print(dic[0][0] if n<=1 or dic[0][1] != dic[1][1] else dic[1][0])
print(max(lst)-min(lst))