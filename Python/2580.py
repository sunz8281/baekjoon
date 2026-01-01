sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j]==0]
length = len(blank)

def dfs(n):
    if n>=length: return True
    x, y = blank[n]
    numbers = [1] * 10
    for i in range(9):
        numbers[sudoku[x][i]] = 0
        numbers[sudoku[i][y]] = 0
        numbers[sudoku[x//3*3+i//3][y//3*3+i%3]] = 0
    for i in range(1, 10):
        if numbers[i]==0: continue
        sudoku[x][y] = i
        if dfs(n+1): return True

    sudoku[x][y] = 0
    return False

dfs(0)
for i in range(9):
    print(*sudoku[i])