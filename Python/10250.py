t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    floor = (n-1)%h+1
    num = (n+(h-1))//h
    print("%d%02d" %(floor, num))