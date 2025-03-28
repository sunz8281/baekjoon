while (s:=input()) != '.':
    lst = []
    for c in s:
        if c not in '[]()': continue
        if c == '[' or c=='(':
            lst.append(c)
        else:
            if lst:
                c2 = lst.pop()
                if (c==']' and c2!='[') or (c==')' and c2!='('):
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if lst: print('no')
        else : print('yes')

