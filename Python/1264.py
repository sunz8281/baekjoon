lst = ['a', 'e', 'i', 'o', 'u']
while (s:=input().lower())!='#':
    print(sum([s.count(i) for i in lst]))