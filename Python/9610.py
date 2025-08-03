cnt = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0, 'AXIS': 0}
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x>0 and y>0:
        cnt['Q1'] += 1
    elif x < 0 < y:
        cnt['Q2'] += 1
    elif x<0 and y<0:
        cnt['Q3'] += 1
    elif x > 0 > y:
        cnt['Q4'] += 1
    else:
        cnt['AXIS'] += 1

for key, value in cnt.items():
    print(f'{key}: {value}')
