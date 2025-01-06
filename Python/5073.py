while True:
    a, b, c = sorted(map(int, input().split()))
    if a == b == c == 0: break
    elif a + b > c:
        if a == b == c: print("Equilateral")
        elif (a==b) or (b==c): print("Isosceles")
        else: print("Scalene")
    else: print("Invalid")