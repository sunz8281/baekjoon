import sys
input = sys.stdin.readline
cnt = {}
for _ in range(int(input())):
    n = int(input())
    if n in cnt: cnt[n] += 1
    else: cnt[n] = 1

for i in sorted(cnt):
    for j in range(cnt[i]): print(i)