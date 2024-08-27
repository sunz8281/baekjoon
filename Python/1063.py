xList = [1, -1, 0, 0, 1, -1, 1, -1]
yList = [0, 0, -1, 1, 1, 1, -1, -1]
charList = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

King, Rock, N = map(str, input().split())
N = int(N)

King = list(King)
Rock = list(Rock)

King[0], King[1] = ord(King[0]), int(King[1])
Rock[0], Rock[1] = ord(Rock[0]), int(Rock[1])

for i in range(N):
    move = input()

    KingX, KingY = King[0] + xList[charList.index(move)], King[1] + yList[charList.index(move)]
    RockX, RockY = Rock[0] + xList[charList.index(move)], Rock[1] + yList[charList.index(move)]

    if (ord('A') > KingX or KingX > ord('H')) or (1>KingY or KingY>8): continue
    if KingX == Rock[0] and KingY == Rock[1]:
        if (ord('A') > RockX or RockX > ord('H')) or (1>RockY or RockY>8): continue
        Rock[0] = RockX
        Rock[1] = RockY

    King[0] = KingX
    King[1] = KingY

print(chr(King[0])+str(King[1]))
print(chr(Rock[0])+str(Rock[1]))