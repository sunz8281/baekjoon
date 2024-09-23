import sys

def calc(a, b):
    return b*100//a

x, y = map(int, input().split())
z = calc(x, y)
if z>=99:
    print(-1)
    sys.exit(0)

cnt = 0
while True:
    x = x+100
    y = y+100
    newz = calc(x, y)
    cnt+=100
    if newz >= z+1: break

while True:
    x = x-1
    y = y-1
    newz = calc(x, y)
    if newz <= z: break
    cnt-=1

print(cnt)
