import sys
# A(x1, y2), B(x2, y2), C(x3, y3) 입력
x1, y1, x2, y2, x3, y3 = map(float, input().split())

if (y1-y2)*(x2-x3) == (y2-y3)*(x1-x2):
    print(float(-1))
    sys.exit(0)

AB = ((x1-x2)**2 + (y1-y2)**2)**0.5
BC = ((x2-x3)**2 + (y2-y3)**2)**0.5
CA = ((x3-x1)**2 + (y3-y1)**2)**0.5

res1 =(AB + BC)*2
res2 =(BC + CA)*2
res3 =(CA + AB)*2

print(max(res1, res2, res3)-min(res1, res2, res3))