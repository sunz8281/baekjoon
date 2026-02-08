import sys
input = sys.stdin.readline

while n:=int(input()):
    i=0
    result=0
    while n:
        i+=1
        x = n%10
        n = n//10
        factorial = 1
        for j in range(1, i):
            factorial *= j+1
        result += factorial*x
    print(result)