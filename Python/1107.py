n = int(input())
m = int(input())
broken = [0] * 10
if m!=0:
    for x in map(int, input().split()):
        broken[x] = 1

def is_broken(num):
    for c in str(num):
        if broken[int(c)]: return True
    return False

result = abs(n-100)
for i in range(1000001):
    if is_broken(i): continue
    result = min(result, len(str(i)) + abs(n - i))
print(result)