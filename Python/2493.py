n = int(input())
tower = list(map(int, input().split()))

stack = []
for i in range(n):
    result = -1
    while stack:
        if tower[stack[-1]] < tower[i]:
            stack.pop()
        else:
            result = stack[-1]
            break
    print(result+1, end=' ')
    stack.append(i)