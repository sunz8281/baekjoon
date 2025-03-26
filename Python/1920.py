import sys
input = sys.stdin.readline

n = int(input())
lst1 = set(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))
for i in lst2:
    print(int(i in lst1))