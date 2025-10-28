moems = {'a', 'e', 'i', 'o', 'u'}
n, c = map(int, input().split())
lst = sorted(tuple(input().split()))

result = []

def check():
    jaem_cnt, moem_cnt = 0, 0
    for item in result:
        if item in moems: moem_cnt += 1
        else: jaem_cnt += 1

    if jaem_cnt < 2 or moem_cnt < 1: return False
    return True

def backtracking(x, idx):
    if x==0:
        if check():
            print(''.join(result))
        return

    for i in range(idx, c-x+1):
        result.append(lst[i])
        backtracking(x-1, i+1)
        result.pop()

backtracking(n, 0)