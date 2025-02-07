h, m, s = map(int, input().split())
s += int(input())
print((h+(m+s//60)//60)%24 ,(m+s//60)%60,s%60)