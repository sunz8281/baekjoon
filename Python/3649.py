import sys
input = sys.stdin.readline

while 1:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lst = sorted([int(input()) for _ in range(n)])

        start, end = 0, n - 1

        while start < end:
            if lst[start] + lst[end] > x:
                end -= 1
            elif lst[start] + lst[end] < x:
                start += 1
            else:
                print('yes', lst[start], lst[end])
                break
        else:
            print('danger')
    except: break