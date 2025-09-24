n = input()
if not ('7' in n or int(n)%7 == 0) :
    print(0)
elif not '7' in n and int(n)%7 == 0 :
    print(1)
elif '7' in n and int(n)%7 != 0 :
    print(2)
elif '7' in n and int(n)%7 == 0 :
    print(3)