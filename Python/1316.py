cnt = 0
for _ in range(int(input())):
    alpha = [False]*65
    s = input() + ' '
    for i in range(len(s)-1):
        if alpha[ord(s[i])-65]:
            cnt-=1
            break
        if s[i] == s[i+1]:
            continue
        alpha[ord(s[i])-65] = True
    cnt+=1
print(cnt)