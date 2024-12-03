n = int(input())
lst = list(map(int, input().split()))
count = [0]*n
for i in range(n):
    for j in range(i+1, n):
        m = (lst[i]-lst[j])/(i-j)
        y = lst[i] - m*i
        flag = True
        for k in range(i+1, j):
            if lst[k] >= m*k + y :
                flag = False
                break
        if flag:
            count[i] += 1
            count[j] += 1

print(max(count))