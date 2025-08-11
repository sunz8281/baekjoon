for i in range(int(input())):
    s = input(f'String #{i+1}\n')
    for c in s:
        print(chr((ord(c)-64)%26+65), end='')
    print('\n')