from itertools import combinations

while True:
    lst = list(input().split())
    if lst.pop(0) == '0': break
    print('\n'.join(' '.join(comb) for comb in combinations(lst, 6)))
    print()
