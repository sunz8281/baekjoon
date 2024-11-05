n = int(input())
arr = [0]*int(n**(1/2)+1)
for i in range(2, int((len(arr)+1)**(1/2)+1)):
    if arr[i]: continue
    for j in range(i+i, len(arr), i):
        arr[j] = 1

arr2 = [i for i in range(2, len(arr)) if arr[i]==0]

while n>1:
    flag = True
    for i in arr2:
        if n%i==0:
            flag = False
            n=n//i
            print(i)
            break
    if flag:
        print(n)
        break
