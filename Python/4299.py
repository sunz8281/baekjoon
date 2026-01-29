hap, cha = map(int, input().split())
a, b = hap+cha, hap-cha
if a%2 or b%2 or hap<cha: print(-1)
else: print(max(a,b)//2, min(a,b)//2)