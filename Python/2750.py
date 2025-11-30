n = int(input())
lst = [int(input()) for _ in range(n)]
print(*sorted(lst), sep='\n')