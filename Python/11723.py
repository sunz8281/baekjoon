import sys

S = [0]*20

for _ in range(int(input())):
    s, *n = sys.stdin.readline().split()
    if n: n = int(n[0])-1

    if s=="add" : S[n]=1
    elif s=="remove" : S[n]=0
    elif s=="check" : print(S[n])
    elif s=="toggle" : S[n] = int(not S[n])
    elif s=="all" : S = [1]*20
    elif s=="empty" : S = [0]*20
