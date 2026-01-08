s = input()
bomb = input()
len_bomb = len(bomb)

stack = []
for i in range(len(s)):
    stack.append(s[i])
    while ''.join(stack[-len_bomb:]) == bomb:
        for _ in range(len_bomb):
            del stack[-1]

if stack:
    print(''.join(stack))
else:
    print("FRULA")