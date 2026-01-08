s = input()
bomb = list(input())
len_bomb = len(bomb)

stack = []
for i in range(len(s)):
    stack.append(s[i])
    while stack[-len_bomb:] == bomb:
        del stack[-len_bomb:]


if stack:
    print(''.join(stack))
else:
    print("FRULA")