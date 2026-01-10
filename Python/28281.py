n, x = map(int, input().split())
prices = list(map(int, input().split()))
min_price = max(prices)*2
for i in range(n-1):
    min_price = min(min_price, prices[i] + prices[i+1])
print(min_price*x)