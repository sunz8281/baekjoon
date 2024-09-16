arr = [0]*43
for _ in range(10):
    arr[(int(input()))%42] = 1
print(arr.count(1))