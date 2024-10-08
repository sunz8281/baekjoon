n, b = input().split()
n = list(n)
b = int(b)

deci = 0
for i in range(len(n)):
    deci *= b
    if n[i].isalpha():
        n[i] = ord(n[i]) - 55
    deci += int(n[i])
print(deci)