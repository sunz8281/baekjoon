import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    c, *n = input().split()
    if n: lst.append(int(*n))
    elif c[0]=='e': print(int(len(lst)==0))
    elif c[0]=='p': print(lst.pop() if lst else -1)
    elif c[0]=='t': print(lst[-1] if lst else -1)
    elif c[0]=='s': print(len(lst))

