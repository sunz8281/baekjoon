n = int(input())
foods = input()
for i in range(n-1):
    mine, friend = foods[:i+1], foods[i+1:]
    if (mine.count('L')!=friend.count('L')
        and mine.count('O')!=friend.count('O')):
        print(len(mine))
        exit(0)
print(-1)