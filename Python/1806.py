n, s = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, 0
min_len = 100001
current_sum = 0
while True:
    while (current_sum < s or left > right) and right < n:
        current_sum += lst[right]
        right += 1

    while current_sum >= s and left < right:
        min_len = min(min_len, right-left)
        current_sum -= lst[left]
        left += 1

    if right >= n: break

if min_len == 100001:
    print(0)
else:
    print(min_len)