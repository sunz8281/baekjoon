n = int(input())
lst = [int(input()) for _ in range(n)]
print("Junhee is" + (" " if sum(lst) > n//2 else " not ") +"cute!")