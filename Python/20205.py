n, k = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(n)]
for i in range(n*k):
    for j in range(n*k):
        print(image[i//k][j//k], end=" ")
    print()