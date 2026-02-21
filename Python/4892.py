i=0
while True:
    i+=1
    n=int(input())
    if n==0: break
    result = (n*3+1)//2*3//9
    print(f"{i}. {'odd' if (n*3)%2 else 'even'} {result}")