n = int(input())
lst = list(map(int, input().split()))

left = [0] * n
right = [0] * n
for i in range(1, n):
    for j in range(i):
        if lst[j] < lst[i]:
            left[i] = max(left[i], left[j]+1)
    for j in range(i):
        if lst[n-j-1] < lst[n-i-1]:
            right[n-i-1] = max(right[n-i-1], right[n-j-1]+1)

mx = 0
for i in range(n):
    length = left[i] + right[i] + 1
    mx = max(mx, length)
print(mx)