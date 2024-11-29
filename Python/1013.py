from collections import deque

def case1(st):
    global last
    last = 0
    x = 0
    for _ in range(2):
        x = st.popleft()
        if x == 1:
            return False
    while x == 0:
        x = st.popleft()

    while st:
        if st[0] == 0:
            break
        last = st.popleft()
    return st

def case2(st):
    global last
    x = st.popleft()
    if x == 0:
        return False
    return st

for i in range(int(input())):
    s = deque(map(int, list(input())))
    last = 0
    flag = True
    while s:
        x = s.popleft()
        try:
            if x == 1:
                result = case1(s.copy())
                if type(result) == bool:
                    flag = False
                    break
                s = result

            elif last == 1 and x == 0:
                result1 = case1(deque([0]) + s.copy())
                result2 = case2(s.copy())
                if type(result1) == deque:
                    s = result1
                elif type(result2) == deque:
                    s = result2
                    last = 0
                else:
                    flag = False
                    break

            else:
                result = case2(s.copy())
                if type(result) == bool:
                    flag = False
                    last = 0
                    break
                s = result

        except IndexError:
            flag = False

    print("YES" if flag else "NO")