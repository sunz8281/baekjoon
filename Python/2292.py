n = int(input())

result = 0
num = 1
while True:
    num += result*6
    result += 1
    if num>=n:
        break

print(result)