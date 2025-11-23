height = {'Es': 21, 'Stair': 17}
result = 0
for l in open(0):
    a, b = l.split()
    result += height[a] * int(b)
print(result)