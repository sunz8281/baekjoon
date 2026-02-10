n = int(input())
while True:
    x = sum(map(int, str(n)))
    if n%x==0: break
    n+=1
print(n)
