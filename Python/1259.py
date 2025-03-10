while True:
    n = input()
    if n == '0': break
    if n[:len(n)//2] == n[:len(n)//2+(-1 if len(n)/2==len(n)//2 else 0):-1]:
        print('yes')
    else: print('no')