import math
a, b = map(int, input().split())
c, d = map(int, input().split())
x, y = a/b, c**2*math.pi/d
print(("Slice of" if x>y  else "Whole")+" pizza")