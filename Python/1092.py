import sys

n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)

m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

if box[0]>crane[0]:
    print(-1)
    sys.exit()

cnt = 0
while box:
    for c in crane:
        for b in box:
            if c>=b:
                box.remove(b)
                break
    cnt+=1

print(cnt)