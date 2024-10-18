for _ in range(int(input())):
    money = int(input())
    q = money//25
    money = money%25
    d = money//10
    money = money%10
    n = money//5
    money = money%5
    p = money
    print(q, d, n, p)