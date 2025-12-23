n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start = 1
end = house[-1] - house[0]
result = 1

while start <= end:
    mid = (start + end) // 2
    current = house[0]
    count = 1

    for i in range(n):
        if house[i] >= mid + current:
            current = house[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)