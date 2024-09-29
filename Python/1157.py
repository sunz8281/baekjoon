s = input().upper()

cnt = []
for i in range(26):
    cnt.append(s.count(chr(i+65)))

if cnt.count(max(cnt))>1:
    print("?")
else:
    print(chr(cnt.index(max(cnt))+65))