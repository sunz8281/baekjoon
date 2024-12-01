n = int(input())
s1 = list(input())
for _ in range(n-1):
    s2 = list(input())
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            s1[i] = '?'

print("".join(s1))