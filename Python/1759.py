from itertools import combinations

n, c = map(int, input().split())
lst = list(input().split())
moems = list(filter(lambda x: x in ('a', 'e', 'i', 'o', 'u'), lst))
jaems = list(filter(lambda x: x not in ('a', 'e', 'i', 'o', 'u'), lst))

result = []
max_moem = min(n-2, len(moems))
for i in range(1, max_moem+1):
    for comb_moem in combinations(moems, i):
        for comb_jaem in combinations(jaems, n-i):
            result.append(''.join(sorted([*comb_moem, *comb_jaem])))
print('\n'.join(sorted(result)))