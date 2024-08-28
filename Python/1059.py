import sys

L = int(input())
S = list(map(int, input().split()))
n = int(input())
cnt = 0

S.sort()
S.insert(0, 0)

for i in range(L+1):
    if S[i]==n:
        print(0)
        sys.exit(0)

    if S[i]>n:
        start, end = S[i-1]+1, S[i]-1
        break

for i in range(start, end+1):
    for j in range(i+1, end+1):
        if i<=n<=j:
            cnt +=1

print(cnt)