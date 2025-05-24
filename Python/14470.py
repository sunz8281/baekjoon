a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

s1 = ((-a + (b if b<0 else 0))*c) if a<0 else 0
s2 = d if a < 0 < b else 0
s3 = (b - (0 if a < 0 < b else a))*e

print(s1+s2+s3)