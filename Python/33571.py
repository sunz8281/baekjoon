hole = ["A", "a", "B", "b", "D", "d", "e", "g", "O", "o", "P", "p", "Q", "q", "R", "@"]
s = input()
cnt = 0
for c in s:
    if c == "B": cnt += 2
    elif c in hole: cnt += 1
print(cnt)