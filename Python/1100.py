lst = [input() for _ in range(8)]
print([lst[i][j] for j in range(8) for i in range(8) if not (i+j)%2].count('F'))