memo = [0, 1, 1]
for i in range(int(input())):
    n = int(input())
    for j in range(len(memo), n+1):
        memo.append(memo[j-2] + memo[j-3])
    print(memo[n])