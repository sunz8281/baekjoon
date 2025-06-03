lst = ["R", "S", "P"]
for _ in range(int(input())):
    p = 0
    for _ in range(int(input())):
        a, b = map(lst.index, input().split())
        if (a+1)%3 == b: p+=1
        elif (b+1)%3 == a: p-=1
    print("Player 1" if p>0 else "Player 2" if p<0 else "TIE")