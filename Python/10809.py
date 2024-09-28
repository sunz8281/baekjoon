s = list(input())
print(*[s.index(chr(c)) if chr(c) in s else -1 for c in range(97, 123)])