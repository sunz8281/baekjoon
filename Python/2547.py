for _ in range(int(input())):
    _=input()
    n=int(input())
    candy = sum(int(input()) for i in range(n))
    if candy%n==0:
        print("YES")
    else:
        print("NO")