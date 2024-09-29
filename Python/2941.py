d = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
cnt = 0
for i in range(8):
    s = s.replace(d[i], ' ')

print(len(s))