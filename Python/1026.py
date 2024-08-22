n = int(input())
A = list(map(int, input().split())) # 1 1 1 6 0
B = list(map(int, input().split())) # 2 7 8 3 1
result = 0
BsortA = []

sortA = sorted(A) # 0 1 1 1 6
sortB = sorted(B) # 1 2 3 7 8

for i in range(n):
    BsortA.append(sortA[n - sortB.index(B[i])- 1])
    sortA[n - sortB.index(B[i])- 1] -=1
    sortB[sortB.index(B[i])] -= 1

for i in range(n):
    result += BsortA[i]*B[i]
print(result)