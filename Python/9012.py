for _ in range(int(input())):
    s = input()
    l = 0
    for c in s:
        if c=='(': l+=1
        else: l-=1
        if l<0:
            print('NO')
            break
    else:
        if l!=0: print('NO')
        else: print('YES')