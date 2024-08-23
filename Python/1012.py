n, m = map(int, input().split())
arr = list(map(int, input().split()))
queue = []
result = 0
start = 1
for i in range(1,n+1):
    queue.append(i)

for i in range(m):
    result += min((queue.index(start)-queue.index(arr[i])+n)%n, (queue.index(arr[i])-queue.index(start)+n)%n)
    start = queue[(queue.index(arr[i])+1+n)%n]
    queue.remove(arr[i])
    n-=1
   

print(result)