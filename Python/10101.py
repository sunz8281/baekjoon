[a, b, c] = [int(input()) for _ in range(3)]
if a+b+c == 180:
    if a==b==c: print('Equilateral')
    elif a==b or a==c or b==c: print('Isosceles')
    else: print('Scalene')
else: print("Error")