n = int(input())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[1], x[0]))

end = 0
cnt = 0
for lstart, lend in lst:
    if end <= lstart:
        cnt += 1
        end = lend

print(cnt)