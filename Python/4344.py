c = int(input())
lst = [list(map(int, input().split()))[1:] for _ in range(c)]
for i in range(c):
    avg = sum(lst[i]) / len(lst[i])
    print(f"{len(list(filter(lambda x:x>avg, lst[i]))) / len(lst[i]) * 100:.3f}%")
