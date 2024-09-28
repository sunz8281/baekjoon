d = [i for i in range(3, 11) for _ in range(3)]
d.insert(15, 8)
d.append(10)

print(sum([d[ord(i)-65] for i in input()]))