arr = [i for i in range(1, 31)]

for _ in range(28):
    n = int(input())
    arr.remove(n)

print(arr[0])
print(arr[1])