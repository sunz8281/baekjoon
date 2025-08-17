n, d = map(int, input().split())
rules = {1: {'d':'q','b':'p','q':'d','p':'b'}, 2: {'d':'b','b':'d','q':'p','p':'q'}}
for _ in range(n):
    print(''.join(rules[d][c] for c in input()))