for _ in range(int(input())):
    n, s = input().split()
    print("".join(c*int(n) for c in s))