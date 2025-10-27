from collections import deque

for i in range(int(input())):
    s = input()
    n = map(int, input().split())
    lst = deque(input()[1:-1].split(','))
    if lst[0] == '': lst.popleft()
    R = False
    try:
        for c in s:
            if c == 'R': R = not R
            elif R: lst.pop()
            else: lst.popleft()
        if R: lst.reverse()
        print('['+','.join(lst)+']')
    except:
        print('error')