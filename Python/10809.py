s = input()
print(*[s.find(chr(c)) for c in range(97, 123)])