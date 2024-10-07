paper = [[0]*100 for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

count = sum(row.count(1) for row in paper)
print(count)
