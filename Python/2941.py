d = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
cnt = 0
for i in range(8):
    cnt+=s.count(d[i])
    s = s.replace(d[i], ' ')

s = s.replace(' ', '')
print(cnt+len(s))