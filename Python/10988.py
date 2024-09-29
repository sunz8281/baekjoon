s = input()
flag = 1
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        flag=0
        break
print(flag)