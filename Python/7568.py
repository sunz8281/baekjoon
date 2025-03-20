n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
cnt = [0] * n
for i in range(n):
    for j in range(i+1, n):
        if lst[i][0]>lst[j][0] and lst[i][1]>lst[j][1]:
            cnt[j] += 1
        elif lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
            cnt[i] += 1
    print(cnt[i]+1, end=' ')
