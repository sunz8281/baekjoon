n = int(input())
result = [0]*26
for _ in range(n):
    a, b = input().split()
    for i in range(26):
        alphabet = chr(i+97)
        result[i] += max(a.count(alphabet), b.count(alphabet))
print('\n'.join(map(str, result)))
