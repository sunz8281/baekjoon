xList = []
for i in range(9):
    xList.append(int(input()))

print(max(xList))
print(xList.index(max(xList))+1)