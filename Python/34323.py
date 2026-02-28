n, m, s = map(int, input().split())
print(int(min(m*s, (m+1)*s*(100-n)//100)))