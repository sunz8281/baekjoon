n, m = map(int, input().split())

color = []
result = []
for _ in range(n):
    color.append(list(str(input())))

for x in range(n-7):
    for y in range(m-7):
        x1=0
        x2=0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if((i+j)%2):
                    if(color[i][j]=='B'):
                        x1+=1
                    else:
                        x2+=1
                else:
                    if(color[i][j]=='W'):
                        x1+=1
                    else:
                        x2+=1
        result.append(x1)
        result.append(x2)

print(min(result))