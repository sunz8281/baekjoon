n, m = map(int, input().split())

chickens = []
homes = []
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 1:
            homes.append((i, j))
        elif l[j] == 2:
            chickens.append((i, j))

len_chickens = len(chickens)
len_homes = len(homes)
survive_chickens = [0]*len_chickens

def check_distance():
    result = 0
    for home in homes:
        distance = []
        for i in range(len_chickens):
            if survive_chickens[i] == 0: continue
            distance.append(abs(chickens[i][0] - home[0]) + abs(chickens[i][1] - home[1]))
        result += min(distance)
    return result

def choice_chicken(x, cnt):
    if cnt==0:
        return check_distance()

    distance = []
    for i in range(x+1, len_chickens-cnt+1):
        survive_chickens[i] = 1
        distance.append(choice_chicken(i, cnt-1))
        survive_chickens[i] = 0
    return min(distance)

print(choice_chicken(-1, m))


