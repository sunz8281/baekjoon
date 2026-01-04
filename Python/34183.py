n, m, a, b = map(int, input().split())
need = n*3-m
if need<=0: print(0)
else: print(need*a+b)