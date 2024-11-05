n = int(input())
while n != -1:
    arr = [1]
    for i in range(2, int(n**(1/2))+1):
        if n%i==0:
            arr.append(i)
            arr.append(n//i)
    if sum(arr) == n:
        print(f'{n} = {" + ".join(map(str, sorted(arr)))}')
    else:
        print(f'{n} is NOT perfect.')
    n = int(input())