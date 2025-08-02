x=[*open(0)][1]
print('A' if x.count('A')>x.count('B') else 'B' if x.count('A')<x.count('B') else 'Tie')