n, a, b = map(int, input().split())
print("Bus" if n>b or a<b else "Subway" if a>b else "Anything")