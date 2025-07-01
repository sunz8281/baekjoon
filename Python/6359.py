for _ in range(int(input())):
    n = int(input())
    lst = [1 for i in range(n + 1)]
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            lst[j] = not lst[j]
    print(lst.count(1)-1)