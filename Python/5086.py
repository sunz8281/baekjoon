while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if not b%a: print("factor")
    elif not a%b: print("multiple")
    else: print("neither")