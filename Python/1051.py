import sys

n, m = map(int, input().split())
square = []
for _ in range(n):
    square.append(list(input()))

for i in range(min(n, m) ,0, -1): #정사각형의 크기
    for j in range(n-i+1): #시작 y좌표
        for k in range(m-i+1): #시작 x좌표
            if square[j][k] == square[j][k+i-1] == square[j+i-1][k]== square[j+i-1][k+i-1]:
                print(i*i)
                sys.exit(0)
