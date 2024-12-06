A, B = input().split()

maxCount = 0
for i in range(len(B)-len(A)+1):
    x = [A[j]==B[i+j] for j in range(len(A))].count(True)
    if x > maxCount:
        maxCount = x

print(len(A)-maxCount)