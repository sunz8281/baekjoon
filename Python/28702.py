[a, b, c] = [input() for _ in range(3)]
res = int(a)+3 if a.isdigit() else int(b)+2 if b.isdigit() else int(c)+1
print((res if res%5 else "Buzz") if res%3 else ("Fizz" if res%5 else "FizzBuzz"))