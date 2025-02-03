def f(k):
    global prime
    for i in range(2, int(k**0.5)+1):
        if not prime[i]: continue
        for j in range(i*i, k+1, i):
            prime[j] = False

lst = [int(input())]
while lst[-1]:
    lst.append(int(input()))
lst.pop()
prime = [False, False] + [True] * (2*(max(lst))+1)
f(2*max(lst))

for i in lst:
    print(prime[i+1:i*2+1].count(True))
