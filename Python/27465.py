def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

n = int(input())
while is_prime(n): n+=1
print(n)