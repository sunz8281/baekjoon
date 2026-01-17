for i in range(int(input())):
    n, s, d = map(int, input().split())
    result = 0
    for j in range(n):
        di, vi = map(int, input().split())
        if di <= d*s: result += vi
    print(f"Data Set {i+1}:\n{result}\n")