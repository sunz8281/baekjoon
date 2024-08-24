import sys
sys.setrecursionlimit(10000) 

aX = [-1, 1, 0, 0]
aY = [0, 0, -1, 1]

def f(X, Y):

    arr[Y][X] = 2
    for i in range(4):
        nX = X+aX[i]
        nY = Y+aY[i]
        if 0>nX or nX>=M or 0>nY or nY>=N: continue
        if arr[nY][nX] == 1:
            f(nX, nY)

t = int(input())
for _ in range(t):
    cnt = 0
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)] # 0이 M개 들어있는 리스트 N개를 arr에 할당
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if(arr[i][j] == 1):
                f(j, i)
                cnt += 1
    print(cnt)
