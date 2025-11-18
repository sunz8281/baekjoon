n = int(input())
terminal = {}
for _ in range(n):
    d, c = input().split()
    terminal[d] = int(c)
jinju = terminal['jinju']
print(jinju)
print(len(list(filter(lambda x: x>jinju, terminal.values()))))