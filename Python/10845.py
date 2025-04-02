from collections import deque
q = deque()
for line in [*open(0)][1:]:
    c, *n = line.split()
    if n: q.append(int(*n))
    elif c[0]=='e': print(int(len(q)==0))
    elif c[0]=='p': print(q.popleft() if q else -1)
    elif c[0]=='s': print(len(q))
    elif c[0]=='f': print(q[0] if q else -1)
    else: print(q[-1] if q else -1)