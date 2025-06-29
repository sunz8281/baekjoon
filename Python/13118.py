lst = list(map(int, input().split()))
x, *_ = map(int, input().split())
for i in range(4):
    if lst[i]==x:
        print(i+1, end='')
        break
else:
    print(0)