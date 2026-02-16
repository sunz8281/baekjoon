n = int(input())
result = 0
for i in range(n):
    p = int(input())
    number, pot = p//10, p%10
    result += number**pot
print(result)