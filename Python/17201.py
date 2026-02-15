n,s=int(input()),list(map(int,input()))
for i in range(n*2-1):
    if s[i]+s[i+1]!=3:
        print("No")
        exit(0)
print("Yes")