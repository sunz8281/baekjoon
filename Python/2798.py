n, m = map(int, input().split())
card = list(map(int, input().split()))
mx = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            hap = card[i] + card[j] + card[k]
            if m >= hap > mx:
                mx = hap

print(mx)
