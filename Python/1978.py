_ = input()
num = list(map(int, input().split()))
arr = [0]*(max(num)+1)
arr[1] = 1
for i in range(2, int(max(num)**(1/2))+1):
    if arr[i]: continue
    for j in range(i+i, max(num)+1, i):
        arr[j] = 1
print([0 if arr[i] else 1 for i in num].count(1))